# request-boost

A simple package for hitting multiple URLs and performing get requests in parallel.

<p align="center">
<a href="https://pypi.org/project/request-boost/"><img src="https://img.shields.io/pypi/pyversions/request-boost" alt="Go to https://pypi.org/project/request-boost/"/></a>
<a href="https://pypi.org/project/request-boost/"><img src="https://img.shields.io/pypi/v/request-boost" alt="Go to https://pypi.org/project/request-boost/"/></a>
<a href="https://pypi.org/project/request-boost/"><img src="https://img.shields.io/pypi/status/request-boost" alt="Go to https://pypi.org/project/request-boost/"/></a>
<a href="https://pypi.org/project/request-boost/"><img src="https://img.shields.io/pypi/format/request-boost" alt="Go to https://pypi.org/project/request-boost/"/></a>
<a href="https://pypistats.org/packages/request-boost"><img src="https://img.shields.io/pypi/dm/request-boost"/></a>
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
