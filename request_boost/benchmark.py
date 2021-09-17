# coding:utf-8
"""
Name       : benchmark
Author     : Kuldeep Singh Sidhu
GitHub     : https://github.com/singhsidhukuldeep
Description:
"""

# !pip install request-boost tqdm plotly
from request_boost import boosted_requests
from datetime import datetime as dt
from tqdm.auto import tqdm
import plotly.express as px

# Sample data
number_of_sample_urls = 200
urls = [f'https://postman-echo.com/get?random_data={test_no}' for test_no in range(number_of_sample_urls)]
headers = [{'sample_header': test_no} for test_no in range(number_of_sample_urls)]

# Using boosted_requests
wcd = {}
for wc in tqdm(range(100, 0, -3)):
    start = dt.now()
    results = boosted_requests(urls=urls, no_workers=wc, max_tries=10, timeout=5, headers=None)
    wcd[wc] = (dt.now() - start).microseconds

# Plotting using plotly
lists = sorted(wcd.items())
x, y = zip(*lists)
fig = px.bar(
    x=x,
    y=y,
    title=f'<b>High Performance gains</b>(16X) of ' +
          '<b>request_boost</b> on <i>Google Colab (low multi-processing)</i> <br>' +
          '<span style="font-size: 12px;">Based on code in ' +
          '<i>request-boost/benchmark.py</i></span>' +
          '<span style="font-size: 10px;"> using <i>postman-echo.com</i> </span>',
    template='plotly_dark',
)
fig.update_xaxes(
    title_text="Number of workers [no_workers] working in parallel")

fig.update_yaxes(
    title_text="Time Taken [microseconds]", title_standoff=25)
fig.show()
