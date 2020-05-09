#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Collect:
MarketCap
Current Ratio
Total Assets : https://finance.yahoo.com/quote/AAPL/balance-sheet/
Total Debt
PE ratio
PB Ratio
Divident Yield
"""

import csv
import getSymbols
import getURLs
from scraping import s_sync, s_threading

BENCHMARK = False
SIZE = 1
TYPE_OF_SCRAPE = 'threading'

if __name__ == '__main__':

    # Get user input for certain parts of the program
    BENCHMARK = bool(input('Do you want to test benchmarks? (False)')) or False
    SIZE = input('What percent of the list do you want to parse? (1 = 10%)') or 1
    SIZE = int(SIZE)
    TYPE_OF_SCRAPE = input('Which method do you want to use: threading or sync? (threading)') or 'threading'


    list = getSymbols.getList()
    list = list[:(len(list) // 10) * SIZE]
    urls = getURLs.getURLs(list)

    print(f'\nNumber of links: {len(urls)} | Working...')

    if BENCHMARK:
        s_threading.scrape(urls, list) # Threading | Downloaded 1776 in 152.52339005470276 seconds

        # Asyncio contains problems:
        #   - OSError: [WinError 10038] An operation was attempted on something that is not a socket
        # s_asyncio.scrape(urls)

        s_sync.scrape(urls, list) # Sync | Downloaded 1776 in 1157.8334589004517 seconds

    if not BENCHMARK:
        if TYPE_OF_SCRAPE == 'threading':
            s_threading.scrape(urls, list)

        elif TYPE_OF_SCRAPE == 'sync':
            s_sync.scrape(urls)

    print(f'\nFinished.')
