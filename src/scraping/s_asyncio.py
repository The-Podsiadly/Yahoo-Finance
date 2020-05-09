import time
st = time.time()

import os, requests
from . import parseContent

import asyncio
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        response.content_length
        # print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


def scrape(urls):
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(urls))
    duration = time.time() - start_time
    print(f"AsyncIO | Downloaded {len(urls)} sites in {duration} seconds")
