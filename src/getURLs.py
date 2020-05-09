def getURLs(dict):
    URLs = []
    for tick in dict:
        # for tick in list:
        try:
            # URLs.append(f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{tick}?formatted=true&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com')
            URLs.append('http://finance.yahoo.com/quote/' + tick + '/key-statistics?p=' + tick)
        except:
            print('No list')

    return URLs
