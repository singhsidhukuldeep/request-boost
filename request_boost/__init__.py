# coding:utf-8
"""
Name       : utils
Author     : Kuldeep Singh Sidhu
GitHub     : https://github.com/singhsidhukuldeep
Description:
"""

import queue
from urllib import request
from threading import Thread
import json


def boosted_requests(urls, no_workers=8, max_tries=3, timeout=10, headers=None):
    """
    Get data from APIs in parallel by creating workers that process in the background
    :param urls: list of URLS
    :param no_workers: maximum number of parallel processes
    :param max_tries: Maximum number of tries before failing for a specific URL
    :param timeout: Waiting time per request
    :param headers: Headers if any for the URL requests
    :return: List of response for each API (order is maintained)
    """

    class GetRequestWorker(Thread):
        def __init__(self, request_queue, max_tries=3, timeout=10):
            """
            Workers that can pull data in the background
            :param request_queue: queue of the URLs
            :param max_tries: Maximum number of tries before failing for a specific URL
            :param timeout: Waiting time per request
            """
            Thread.__init__(self)
            self.queue = request_queue
            self.results = {}
            self.max_tries = max_tries
            self.timeout = timeout

        def run(self):
            while True:
                if self.queue.qsize() == 0:
                    break
                else:
                    content = self.queue.get()
                    url = content['url']
                    header = content['header']
                    num_tries = content['retry']
                    assert num_tries < self.max_tries, f"Maximum number of attempts reached {self.max_tries}"
                try:
                    _request = request.Request(url)
                    for k, v in header.items():
                        _request.add_header(k, v)
                    response = request.urlopen(_request, timeout=self.timeout)
                except Exception as exp:
                    self.queue.put({'url': url, 'retry': num_tries + 1})
                    continue
                if response.getcode() == 200:
                    self.results[url] = json.loads(response.read())
                    self.queue.task_done()
                else:
                    self.queue.put({'url': url, 'retry': num_tries + 1})

    if headers is None:
        headers = [{} for _ in range(len(urls))]

    assert len(headers) == len(urls), 'Length of headers and urls need to be same'

    url_q = queue.Queue()
    for i in range(len(urls)):
        url_q.put({'url': urls[i], 'retry': 0, 'header': headers[i]})

    workers = []

    for _ in range(min(url_q.qsize(), no_workers)):
        worker = GetRequestWorker(url_q, max_tries=3, timeout=10)
        worker.start()
        workers.append(worker)

    for worker in workers:
        worker.join()

    ret = {}
    for worker in workers:
        ret.update(worker.results)
    return [ret[_url] for _url in urls]
