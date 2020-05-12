from datetime import date
import time, json
import lxml.html
from bs4 import BeautifulSoup as BS

categories = ['Market Cap (intraday)', 'Trailing P/E', 'Price/Book','Total Debt','Current Ratio','Forward Annual Dividend Yield']
today = str(date.today())


JSON = False

def main(content, url, tick):
    '''
    Currently this program is too slow using BS4 but it gets the categories
    we are looking for... 'lxml' was too complicated and had was accurate enough.
    Maybe we can pull the functions directly from BS4 and convert it to 'lxml.xpath'
    to speed this process up?
    '''
    soup = BS(content, "lxml")

    list = {}
    list['Tick'] = tick
    for cat in categories:
        list[cat] = str(soup.find_all('span', string=cat)[0].parent.findNext('td').text)

    with open("Data-" + today + ".json", "a+", newline="") as outfile:
        json.dump(list, outfile)



##################################################################
############    For future    ####################################
##################################################################
    # if not JSON:
    #     content = content.decode('utf8') # Content Type = Bytes
    #     root = lxml.html.fromstring(content)
    #
    # list = {}
    # list['Tick'] = tick
    # with open("Data-" + today + ".json", "a+", newline="") as outfile:
    #     if not JSON:
    #
    #         # tbl = root.xpath('.//*[@data-reactid="78"]//text()')
    #         # print(tbl)
    #         # for i, k in enumerate(tbl):
    #         #     for cat in categories:
    #         #         if k == cat and ('(' in el[i+2] or 1 <= int(el[i+2]) <= 9):
    #         #             list[cat] = el[i+3]
    #         #             print(f'{cat} | {list[cat]}')
    #         #             continue
    #         #         elif k == cat:
    #         #             list[cat] = el[i+2]
    #         #             print(f'{cat} | {list[cat]}')
    #         #             continue
    #         #
    #         #         print(f'{cat} | {k}')
    #
    #         for tbl in root.xpath('.//tbody'):
    #             el = tbl.xpath('.//tr/td//text()')
    #
    #             print(el)
    #
    #             for i, k in enumerate(el):
    #                 for cat in categories:
    #                     if k == cat and ('(' in el[i+2] or 1 <= int(el[i+2]) <= 9):
    #                         list[cat] = el[i+3]
    #                         # print(f'{cat} | {list[cat]}')
    #                         continue
    #                     elif k == cat:
    #                         list[cat] = el[i+2]
    #                         # print(f'{cat} | {list[cat]}')
    #                         continue
    #
    #     # else:
    #         # TODO: Get info from JSON link
    #
    #
    #     print(list)
    #
    #     json.dump(list, outfile)
