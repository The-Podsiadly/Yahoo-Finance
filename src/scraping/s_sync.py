import time
st = time.time()

import os, requests
from . import parseContent

def download_site(url, session, tick):
    with session.get(url) as response:
        parseContent(response.content, url, tick)
        # print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites, ticks):
    with requests.Session() as session:
        for index, url in enumerate(sites):
            download_site(url, session, ticks[index])


def scrape(urls, ticks):
    start_time = time.time()
    download_all_sites(urls, ticks)
    duration = time.time() - start_time
    print(f"Sync | Downloaded {len(urls)} in {duration} seconds")
