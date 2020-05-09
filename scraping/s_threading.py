import time
st = time.time()

import os, requests
from . import parseContent

import concurrent.futures
import threading

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url, tick):
    session = get_session()
    with session.get(url) as response:
        parseContent.main(response.content, url, tick)

def download_all_sites(sites, ticks, workers = 8):
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(download_site, sites, ticks)

def scrape(urls, ticks):
    start_time = time.time()
    download_all_sites(urls, ticks)
    duration = time.time() - start_time
    print(f"Threading | Downloaded {len(urls)} in {duration} seconds")
