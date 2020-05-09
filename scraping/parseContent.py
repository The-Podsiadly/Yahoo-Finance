from datetime import date
import time, json
import lxml.html

categories = ['Market Cap (intraday)', 'Trailing P/E', 'Price/Book','Total Debt','Current Ratio','Forward Annual Dividend Yield']
today = str(date.today())


'''
['Beta (5Y Monthly)', ' ', '0.94',
'52-Week Change', ' ', '3', '-60.63%',
'S&P500 52-Week Change', ' ', '3', '-0.01%',
'52 Week High', ' ', '3', '86.71',
'52 Week Low', ' ', '3', '22.18',
'50-Day Moving Average', ' ', '3', '31.55',
'200-Day Moving Average', ' ', '3', '57.42']
['Avg Vol (3 month)', ' ', '3', '605.67k',
'Avg Vol (10 day)', ' ', '3', '654.51k',
'Shares Outstanding', ' ', '5', '19.19M',
'Float', ' ', '8.75M',
'% Held by Insiders', ' ', '1', '20.31%',
'% Held by Institutions', ' ', '1', '109.37%',
'Shares Short (Apr 14, 2020)', ' ', '4', '6.67M',
'Short Ratio (Apr 14, 2020)', ' ', '4', '10.56',
'Short % of Float (Apr 14, 2020)', ' ', '4', '122.64%',
'Short % of Shares Outstanding (Apr 14, 2020)', ' ', '4', '28.74%',
'Shares Short (prior month Mar 12, 2020)', ' ', '4', '6.6M']
['Forward Annual Dividend Rate', ' ', '4', '0.6',
'Forward Annual Dividend Yield', ' ', '4', '2.31%',
'Trailing Annual Dividend Rate', ' ', '3', '0.50',
'Trailing Annual Dividend Yield', ' ', '3', '1.92%',
'5 Year Average Dividend Yield', ' ', '4', '0.53',
'Payout Ratio', ' ', '4', '11.42%',
'Dividend Date', ' ', '3', 'May 03, 2020',
'Ex-Dividend Date', ' ', '4', 'Mar 29, 2020',
'Last Split Factor', ' ', '2', '3:1',
'Last Split Date', ' ', '3', 'Jun 07, 1992']
['Fiscal Year Ends', ' ', 'Jan 31, 2020',
'Most Recent Quarter', ' ', '(mrq)', 'Jan 31, 2020']
['Profit Margin', ' ', '1.75%',
'Operating Margin', ' ', '(ttm)', '2.52%']
['Return on Assets', ' ', '(ttm)', '2.91%',
'Return on Equity', ' ', '(ttm)', '6.73%']
['Revenue', ' ', '(ttm)', '6.34B',
'Revenue Per Share', ' ', '(ttm)', '250.09',
'Quarterly Revenue Growth', ' ', '(yoy)', '-4.50%',
'Gross Profit', ' ', '(ttm)', '2.11B',
'EBITDA', ' ', '383.19M',
'Net Income Avi to Common', ' ', '(ttm)', '111.08M',
'Diluted EPS', ' ', '(ttm)', '4.38',
'Quarterly Earnings Growth', ' ', '(yoy)', '-20.50%']
['Total Cash', ' ', '(mrq)', '277.08M',
'Total Cash Per Share', ' ', '(mrq)', '11.85',
'Total Debt', ' ', '(mrq)', '614.96M',
'Total Debt/Equity', ' ', '(mrq)', '37.88',
'Current Ratio', ' ', '(mrq)', '1.99',
'Book Value Per Share', ' ', '(mrq)', '67.09']
['Operating Cash Flow', ' ', '(ttm)', '365.07M',
'Levered Free Cash Flow', ' ', '(ttm)', '252.41M']
'''


JSON = False

def main(content, url, tick):

    if not JSON:
        content = content.decode('utf8') # Content Type = Bytes
        root = lxml.html.fromstring(content)

    list = {}
    list['Tick'] = tick
    with open("Data-" + today + ".json", "a+", newline="") as outfile:
        if not JSON:
            
            # tbl = root.xpath('.//*[@data-reactid="78"]//text()')
            # print(tbl)
            # for i, k in enumerate(tbl):
            #     for cat in categories:
            #         if k == cat and ('(' in el[i+2] or 1 <= int(el[i+2]) <= 9):
            #             list[cat] = el[i+3]
            #             print(f'{cat} | {list[cat]}')
            #             continue
            #         elif k == cat:
            #             list[cat] = el[i+2]
            #             print(f'{cat} | {list[cat]}')
            #             continue
            #
            #         print(f'{cat} | {k}')

            for tbl in root.xpath('.//tbody'):
                el = tbl.xpath('.//tr/td//text()')

                print(el)

                for i, k in enumerate(el):
                    for cat in categories:
                        if k == cat and ('(' in el[i+2] or 1 <= int(el[i+2]) <= 9):
                            list[cat] = el[i+3]
                            # print(f'{cat} | {list[cat]}')
                            continue
                        elif k == cat:
                            list[cat] = el[i+2]
                            # print(f'{cat} | {list[cat]}')
                            continue

        # else:
            # TODO: Get info from JSON link


        print(list)

        json.dump(list, outfile)
