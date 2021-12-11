# coding:utf-8
"""
Name       : benchmark
Author     : Kuldeep Singh Sidhu
GitHub     : https://github.com/singhsidhukuldeep
Description:
"""

# !pip install request-boost tqdm plotly pandas
from request_boost import boosted_requests
from datetime import datetime as dt
from tqdm.auto import tqdm
import plotly.express as px

# Sample data
number_of_sample_urls = 250
urls = [
    f"https://postman-echo.com/get?random_data={test_no}"
    for test_no in range(number_of_sample_urls)
]
headers = [{"sample_header": test_no} for test_no in range(number_of_sample_urls)]

# Using boosted_requests
wcd = {}
for wc in tqdm(range(45, 0, -1)):
    start = dt.now()
    results = boosted_requests(
        urls=urls, no_workers=wc, max_tries=5, timeout=5, headers=None
    )
    wcd[wc] = int((dt.now() - start).total_seconds() * 1000)

# Plotting using plotly
lists = sorted(wcd.items())
x, y = zip(*lists)
fig = px.bar(
    x=x,
    y=y,
    title=f"<b>High Performance gains</b>(30X) of "
    + "<b>request_boost</b> even on <i>Google Colab (low multi-processing)</i> <br>"
    + '<span style="font-size: 12px;">Based on code in '
    + "<i>request-boost/benchmark.py</i></span>"
    + '<span style="font-size: 10px;"> using <i>postman-echo.com</i> </span>',
    template="plotly_dark",
)
fig.update_xaxes(title_text="Number of workers [no_workers] working in parallel")

fig.update_yaxes(title_text="Time Taken [milliseconds]", title_standoff=25)
fig.show()
