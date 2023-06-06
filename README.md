<h1 align="center">request-boost </h1>

<p align="center">
  
  <a href="https://pypi.org/project/request-boost/">
    <img src="https://github.com/singhsidhukuldeep/request-boost/raw/main/img/benchmark.png" width="1080" alt="Go to https://pypi.org/project/request-boost/">
  </a>
</p>

<p align="center">
<b>A better requests and urllib package.</b></b><br> A simple package for hitting multiple URLs and performing GET/POST requests in parallel.<br>
<a href="https://pypi.org/project/request-boost/"><img src="https://img.shields.io/pypi/pyversions/request-boost" alt="Go to https://pypi.org/project/request-boost/"/></a>
<a href="https://pypi.org/project/request-boost/"><img src="https://img.shields.io/pypi/v/request-boost" alt="Go to https://pypi.org/project/request-boost/"/></a>
<a href="https://pypi.org/project/request-boost/"><img src="https://img.shields.io/pypi/status/request-boost" alt="Go to https://pypi.org/project/request-boost/"/></a>
<!-- <a href="https://pypi.org/project/request-boost/"><img src="https://img.shields.io/pypi/format/request-boost" alt="Go to https://pypi.org/project/request-boost/"/></a> -->
<!-- <a href="https://lgtm.com/projects/g/singhsidhukuldeep/request-boost/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/singhsidhukuldeep/request-boost.svg?logo=lgtm&logoWidth=18"/></a> -->
<a href="https://pypistats.org/packages/request-boost"><img src="https://img.shields.io/pypi/dm/request-boost"/></a>
<!-- <img src="https://visitor-badge.glitch.me/badge?page_id=request_boost" alt="Go to https://pypi.org/project/request-boost/"/> -->
<img src="https://static.pepy.tech/personalized-badge/request-boost?period=total&units=none&left_color=black&right_color=brightgreen&left_text=Total%20Downloads" alt="Go to https://pypi.org/project/request-boost/"/>
</p>

## Setup

```shell
pip install request-boost
```

**Important:** *Virtual Environment is recommended*

## Usage

```python
# Sample data
number_of_sample_urls = 1000
urls = [ f'https://postman-echo.com/get?random_data={test_no}' for test_no in range(number_of_sample_urls) ]
headers = [{'sample_header':test_no} for test_no in range(number_of_sample_urls)]
```

```python
from request_boost import boosted_requests

results = boosted_requests(urls=urls)
print(results)
```

```python
from request_boost import boosted_requests

results = boosted_requests(urls=urls, no_workers=16, max_tries=5, timeout=5, headers=headers, verbose=True, parse_json=True)
print(results)
```

```python
from request_boost import boosted_requests

# Config
number_of_sample_urls = 100

# Sample data
urls = [f'https://postman-echo.com/get?random_data={test_no}' for test_no in range(number_of_sample_urls)]
post_urls = [f'https://postman-echo.com/post' for test_no in range(number_of_sample_urls)]
headers = [{'sample_header': test_no} for test_no in range(number_of_sample_urls)]
data = [{'sample_data': test_no} for test_no in range(number_of_sample_urls)] # Required for POST requests, 
#For POST request data can be just list of empty dict but not NONE

simple_results = boosted_requests(urls=urls, no_workers=16, max_tries=5, timeout=5, headers=None, verbose=False, parse_json=True)
header_results = boosted_requests(urls=urls, no_workers=16, max_tries=5, timeout=5, headers=headers, parse_json=True)
post_results = boosted_requests(urls=post_urls, no_workers=16, max_tries=5, timeout=5, headers=headers, data=data, verbose=True, parse_json=True)
```

## Documentation

<p align="center">
  <a href="https://github.com/singhsidhukuldeep/request-boost/raw/main/img/structure.jpg">
    <img src="https://github.com/singhsidhukuldeep/request-boost/raw/main/img/structure.jpg" width="70%" alt="Go to https://github.com/singhsidhukuldeep/request-boost/raw/main/img/structure.jpg">
  </a>
</p>

```python
boosted_requests(
    urls,
    no_workers=32,
    max_tries=5,
    after_max_tries="assert",
    timeout=10,
    headers=None,
    data=None,
    verbose=True,
    parse_json=True,
)

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
    :param parse_json: Parse response to json [True or False] {Default::True}
    :return: List of response for each API (order is maintained)
```

## Credits

### Maintained by

***Kuldeep Singh Sidhu*** 

Github: [github/singhsidhukuldeep](https://github.com/singhsidhukuldeep)
`https://github.com/singhsidhukuldeep`

Website: [Kuldeep Singh Sidhu (Website)](http://kuldeepsinghsidhu.com)
`http://kuldeepsinghsidhu.com`

LinkedIn: [Kuldeep Singh Sidhu (LinkedIn)](https://www.linkedin.com/in/singhsidhukuldeep/)
`https://www.linkedin.com/in/singhsidhukuldeep/`

### Contributors

<a href="https://github.com/singhsidhukuldeep/request-boost/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=singhsidhukuldeep/request-boost" />
</a>

 The full list of all the contributors is available [here](https://github.com/singhsidhukuldeep/request-boost/graphs/contributors)


[![https://github.com/singhsidhukuldeep](https://forthebadge.com/images/badges/built-with-love.svg)](http://kuldeepsinghsidhu.com)

#### TODO:: Want to contribute?

- [ ] Make the backend used (urllib/request library) an option that the user can choose, by default we use urllib
- [ ] For parallel processing add options for multi-processing along with multi-threading
- [ ] Set-up tests for edge cases and changes verification
- [ ] Set-up CI/CD pipleine (possibly using GitHub actions) to publish changes to PyPi
- [ ] Improeve the doc-strings documentation to add more explanantion and examples
- [ ] Add a message queue to deploy the service across machines
- [ ] Add option to run URL requests with Self signed certificate `verify=False`
- [ ] Add option to supress warnings
- [ ] Add progess bars from tqdm and ascii
- [ ] Add option to add session and auth

## Say Thanks

 If this helped you in any way, it would be great if you could share it with others.

## Steps for publishing to `pypi` [This is just for me, Maybe!]

- `pip3 install setuptools twine`
- Go to project folder
- `python3 setup.py sdist`
- `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`

OR

Go to your project folder and:
```shell
pip3 install setuptools twine

python3 setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

## Current Status

[![Issues](https://img.shields.io/github/issues/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/issues)
[![Contributors](https://badgen.net/github/contributors/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/graphs/contributors)
[![Forks](https://badgen.net/github/forks/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/network/members)
[![Stars](https://badgen.net/github/stars/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/stargazers)
[![Watchers](https://badgen.net/github/watchers/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/watchers)
[![Branches](https://badgen.net/github/branches/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/branches)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python3.5+-1f425f.svg)](https://www.python.org/)
[![repo- size](https://img.shields.io/github/repo-size/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost)
[![Followers](https://img.shields.io/github/followers/singhsidhukuldeep?style=plastic&logo=github)](https://github.com/singhsidhukuldeep?tab=followers)

