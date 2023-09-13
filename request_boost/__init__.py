# coding:utf-8
"""
Name       : __init__
Author     : Kuldeep Singh Sidhu
GitHub     : https://github.com/singhsidhukuldeep
Description:
"""

import json
import queue
from datetime import datetime
from threading import Thread
from urllib import parse, request


def boosted_requests(
    urls,
    no_workers=32,
    max_tries=5,
    after_max_tries="assert",
    timeout=10,
    headers=None,
    data=None,
    verbose=True,
    response_process=None,
    parse_json=True,
):
    """
    Get data from APIs in parallel by creating workers that process in the background
    :param urls: list of URLS
    :param no_workers: maximum number of parallel processes {Default::32}
    :param max_tries: Maximum number of tries before failing for a specific URL {Default::5}
    :param after_max_tries: What to do if not successfull after "max_tries" for a specific URL, 
                            one of {"assert", "break"} {Default::assert}
    :param timeout: Waiting time per request {Default::10}
    :param headers: Headers if any for the URL requests
    :param data: data if any for the URL requests (Wherever not None a POST request is made)
    :param verbose: Show progress [True or False] {Default::True}
    :param parse_json: Parse response to json (ignored if response_process is not None) [True or False] {Default::True}
        If parse_json is False, then response bytes are used
    :param response_process: Callback function to run on request {Default::None}
        Callback recieves response object as argument, and returns tuple (response_ok, data)
           where response_ok [True or False] indicates if response was ok (or else retry is required)
                 data is processed response data
        If response_process is None, then process according to parse_json
    :return: List of response for each API (order is maintained)
    """
    if response_process is not None and not callable(response_process):
        raise ValueError(f'Expected a callable function or None as request_process, got {type(response_process)}')

    start = datetime.now()

    def _printer(inp, end=""):
        print(
            f"\r::{(datetime.now() - start).total_seconds():.2f} seconds::",
            str(inp),
            end=end,
        )

    class GetRequestWorker(Thread):
        def __init__(
            self, request_queue, max_tries=5, after_max_tries="assert", timeout=10, verbose=True, 
            parse_json=True, response_process=None
        ):
            """
            Workers that can pull data in the background
            :param request_queue: queue of the dict containing the URLs
            :param max_tries: Maximum number of tries before failing for a specific URL
            :param after_max_tries: What to do if not successfull after "max_tries" for a specific URL, 
                                    one of {"assert", "break"} {Default::assert}
            :param timeout: Waiting time per request
            :param verbose: Show progress [True or False]
            :param parse_json: Parse response to json [True or False]
            :param response_process: Callback function to run on request [function or None]
                Callback function accepts one argument (response object), returns tuple (response_ok, data)
            """
            Thread.__init__(self)
            self.queue = request_queue
            self.results = {}
            self.max_tries = max_tries
            assert str(after_max_tries).lower() in {"assert", "break"}, """
            'after_max_tries' param CANNOT be anything that you want!
            :param after_max_tries: What to do if not successfull after "max_tries" for a specific URL, 
                                    one of {"assert", "break"} {Default::assert}
            """
            self.after_max_tries = str(after_max_tries).lower()
            self.timeout = timeout
            self.verbose = verbose
            self.parse_json = parse_json
            self.response_process = response_process

        def run(self):
            while True:
                if self.verbose:
                    _printer(f">> {self.queue.qsize()} requests left", end="")
                if self.queue.qsize() == 0:
                    break
                else:
                    content = self.queue.get()
                    url = content["url"]
                    header = content["header"]
                    num_tries = content["retry"]
                    data = content["data"]
                    loc = content["loc"]
                    if num_tries >= self.max_tries:
                        if self.after_max_tries == "assert":
                            assert (
                                num_tries < self.max_tries
                            ), f"Maximum number of attempts reached {self.max_tries} for {content}"
                        elif self.after_max_tries == "break":
                            break
                try:
                    if data is not None:
                        data = parse.urlencode(data).encode()
                        _request = request.Request(url, data=data)
                    else:
                        _request = request.Request(url)
                    for k, v in header.items():
                        _request.add_header(k, v)
                    response = request.urlopen(_request, timeout=self.timeout)
                except Exception as exp:
                    content["retry"] += 1
                    self.queue.put(content)
                    continue
                
                response_ok = response.getcode() == 200
                data = response.read()
                if self.response_process is not None:
                    response_ok, data = self.response_process(response)
                if response_ok:
                    if self.response_process is None:
                        encoding = response.info().get_content_charset("utf-8")
                        decoded_data = data.decode(encoding)
                        self.results[loc] = (
                            json.loads(decoded_data) if self.parse_json else decoded_data
                        )
                    else:
                        self.results[loc] = data
                    self.queue.task_done()
                else:
                    content["retry"] += 1
                    self.queue.put(content)

    if headers is None:
        headers = [{} for _ in range(len(urls))]
    if data is None:
        data = [None for _ in range(len(urls))]

    assert len(headers) == len(
        urls
    ), "Length of headers and urls need to be same OR headers needs to be None"
    assert len(data) == len(
        urls
    ), "Length of data and urls need to be same OR data needs to be None (in case of GET)"

    url_q = queue.Queue()
    for i in range(len(urls)):
        url_q.put(
            {
                "url": urls[i],
                "retry": 0,
                "header": headers[i],
                "loc": i,
                "data": data[i],
            }
        )

    workers = []

    for _ in range(min(url_q.qsize(), no_workers)):
        worker = GetRequestWorker(
            url_q,
            max_tries=max_tries,
            after_max_tries=after_max_tries,
            timeout=timeout,
            verbose=verbose,
            parse_json=parse_json,
            response_process=response_process
        )
        worker.start()
        workers.append(worker)

    for worker in workers:
        worker.join()

    ret = {}
    for worker in workers:
        ret.update(worker.results)
    if verbose:
        _printer(f">> DONE")
    return [ret.get(_) for _ in range(len(urls))]
