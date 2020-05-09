import time
st = time.time()

import os, lxml, xlrd, re, requests
# import asyncio
# import aiohttp



def getURLs(dict):
    URLs = []
    for list in dict:
        for tick in list:
            try:
                URLs.append('http://finance.yahoo.com/quote/' + tick + '/key-statistics?p=' + tick)
            except:
                print('No list')

    return URLs


import concurrent.futures
# import requests
import threading
# import time


thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


def scrape(dict):
    sites = getURLs(dict)
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")


# def download_site(url, session):
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")
#
#
# def download_all_sites(sites):
#     with requests.Session() as session:
#         for url in sites:
#             download_site(url, session)
#
#
# def scrape(dict):
#     sites = getURLs(dict)
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")

# async def download_site(session, url):
#     async with session.get(url) as response:
#         print("Read {0} from {1}".format(response.content_length, url))
#
#
# async def download_all_sites(sites):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for url in sites:
#             task = asyncio.ensure_future(download_site(session, url))
#             tasks.append(task)
#         await asyncio.gather(*tasks, return_exceptions=True)
#
#
# def scrape(dict):
#     sites = getURLs(dict)
#     # sites = [
#     #     "https://www.jython.org",
#     #     "http://olympus.realpython.org/dice",
#     # ] * 80
#     start_time = time.time()
#     asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} sites in {duration} seconds")
