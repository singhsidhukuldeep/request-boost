# request-boost

A simple package for hitting multiple URLs and performing get requests in parallel.

## Current Status

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/singhsidhukuldeep)
[![GitHub pages status](https://img.shields.io/github/deployments/singhsidhukuldeep/request-boost/github-pages)](https://github.com/singhsidhukuldeep/request-boost/deployments/activity_log?environment=github-pages)
[![GitHub up-time BOT](https://badgen.net/uptime-robot/month/ur967659-422c6e77bfb79bb6a47c642c)](https://github.com/singhsidhukuldeep/request-boost/deployments/activity_log?environment=github-pages)
[![Commits](https://img.shields.io/github/last-commit/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/commits/master)
[![DependaBot](https://api.dependabot.com/badges/status?host=github&repo=singhsidhukuldeep/request-boost)](https://dependabot.com/)

[![Issues](https://img.shields.io/github/issues/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/issues)
[![Total Commits](https://badgen.net/github/commits/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/commits/master)
[![Contributors](https://badgen.net/github/contributors/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/graphs/contributors)
[![Forks](https://badgen.net/github/forks/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/network/members)
[![Stars](https://badgen.net/github/stars/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/stargazers)
[![Watchers](https://badgen.net/github/watchers/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/watchers)
[![Branches](https://badgen.net/github/branches/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost/branches)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python3.5+-1f425f.svg)](https://www.python.org/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
[![repo- size](https://img.shields.io/github/repo-size/singhsidhukuldeep/request-boost)](https://github.com/singhsidhukuldeep/request-boost)
[![Followers](https://img.shields.io/github/followers/singhsidhukuldeep?style=plastic&logo=github)](https://github.com/singhsidhukuldeep?tab=followers)

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

results = boosted_requests(urls=urls, no_workers=16, max_tries=5, timeout=5, headers=headers)
print(results)
```

## Documentation

```
boosted_requests(urls, no_workers=8, max_tries=3, timeout=10, headers=None)

Get data from APIs in parallel by creating workers that process in the background
    :param urls: list of URLS
    :param no_workers: maximum number of parallel processes
    :param max_tries: Maximum number of tries before failing for a specific URL
    :param timeout: Waiting time per request
    :param headers: Headers if any for the URL requests
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

 The full list of all the contributors is available [here](https://github.com/singhsidhukuldeep/request-boost/graphs/contributors)


[![website](https://forthebadge.com/images/badges/built-with-love.svg)](http://kuldeepsinghsidhu.com)

## Say Thanks

 If this helped you in any way, it would be great if you could share it with others.
