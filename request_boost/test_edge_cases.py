# coding:utf-8
"""
Name       : test_edge_cases
Author     : Kuldeep Singh Sidhu
GitHub     : https://github.com/singhsidhukuldeep
Description:
"""

# python -m request_boost.test_edge_cases
from . import boosted_requests
from datetime import datetime as dt
from tqdm.auto import tqdm

# Base test case for boosted_requests using https://postman-echo.com
print('BASE TEST CASE')
number_of_sample_urls = 20
urls = [
    f"https://postman-echo.com/get?random_data={test_no}"
    for test_no in range(number_of_sample_urls)
]
headers = [{"sample_header": test_no}
           for test_no in range(number_of_sample_urls)]
wcd = {}
for wc in tqdm(range(45, 0, -1)):
    start = dt.now()
    results = boosted_requests(
        urls=urls, no_workers=wc, max_tries=5, timeout=5, headers=None
    )
    wcd[wc] = int((dt.now() - start).total_seconds() * 1000)
print()

# 12: any way to turn off exception messages?
print("ISSUE:", "https://github.com/singhsidhukuldeep/request-boost/issues/12")
url_ske = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"
urls = [url_ske.format(lemma) for lemma in ["bugler", "hello", "scaper"]]
results = boosted_requests(urls=urls, max_tries=1, after_max_tries="break")
print()
print(results)
print()
