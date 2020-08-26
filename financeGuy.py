from tiingo import TiingoClient
import numpy as np
import pandas as pd
from io import StringIO

#allTickers = pd.read_csv('nasdaqCSV.csv')
#top99 =['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOGL', 'GOOG', 'JNJ', 'V', 'PG', 'NVDA', 'HD', 'MA', 'JPM', 'UNH', 'VZ', 'PYPL', 'DIS', 'ADBE', 'MRK', 'NFLX', 'PFE', 'T', 'INTC', 'BAC', 'CMCSA', 'CRM', 'PEP', 'KO', 'WMT', 'ABT', 'CSCO', 'XOM', 'TMO', 'ABBV', 'CVX', 'MCD', 'COST', 'ACN', 'AMGN', 'BMY', 'NKE', 'NEE', 'MDT', 'AVGO', 'UNP', 'LIN', 'DHR', 'QCOM', 'TXN', 'LLY', 'LOW', 'PM', 'ORCL', 'HON', 'UPS', 'IBM', 'AMT', 'C', 'AMD', 'LMT', 'SBUX', 'MMM', 'BA', 'CHTR', 'WFC', 'BLK', 'FIS', 'RTX', 'INTU', 'NOW', 'SPGI', 'GILD', 'CVS', 'MDLZ', 'ISRG', 'MO', 'TGT', 'CAT', 'BKNG', 'ZTS', 'BDX', 'PLD', 'VRTX', 'ANTM', 'EQIX', 'TMUS', 'CCI', 'CL', 'D', 'CI', 'AXP', 'ATVI', 'DE', 'GS', 'TJX', 'APD', 'CME', 'MS', 'REGN']
top99 = ['AAPL', 'MSFT', 'AMZN']
#print(allTickers)
#allTickers = pd.concat(csv, ignore_index=True)
#listOfTickers = []

#for row in allTickers.iterrows():
    #print(row)
   # if not np.isnan(row == "startDate"): #if the start date is not empty
  #       if  not np.isnan(row == "endDate"): # if the end date is not empty
 #            listOfTickers.append(row[1][0])
#print(listOfTickers)

#listOfTickers = listOfTickers:300]
#print(listOfTickers)

# Set TIINGO_API_KEY in your environment variables in your .bash_profile, OR
# pass a dictionary with 'api_key' as a key into the TiingoClient.

config = {}

# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# If you don't have your API key as an environment variable,
# pass it in via a configuration dictionary.
config['api_key'] = "a17ef094e195b4a09409f0fb1753880fc420154a"

# Initialize
client = TiingoClient(config)

########################################################
# Start of our code ####################################
########################################################
########################################################

#eight_stocks = ["AAPL","GOOGL","MSFT", "AMD", "PYPL","SQ", "TSLA","TMXLF"]

frame = []

for ticker in top99:
    print("***************")
    print(ticker)
    jsonData = client.get_ticker_price(ticker, fmt='json', startDate='2019-08-26',  frequency='daily')
    
    #print(jsonData)
    #here is where u take the difference. each 1st row is the startDate infp and 2nd is the endDate info
    lastYearPrice = 0.0
    thisYearPrice = 0.0
    i =0
    for row in jsonData:
        #print("STOCK: ", ticker,  row['close'])
        if i == 0:
            lastYearPrice = row['close']
        
        thisYearPrice = row['close']
        i += 1
     # % return formula here
    percentReturn = (thisYearPrice / lastYearPrice) * 100
  
    singleStockDataFrame = pd.DataFrame({'Ticker': [ticker], '% Return': [percentReturn]} )
    frame.append(singleStockDataFrame)
   # print()  

YTD_df = pd.concat(frame)

YTD_df = YTD_df.sort_values(by= ['% Return'], ignore_index=True, ascending=False)
# turn data frame to html text
YTD_df.to_html('table.html')
#print(YTD_df)


#ticker_history = client.get_dataframe(eight_stocks,
#                                      frequency='daily',
##                                      metric_name='close',
#                                      startDate='2019-08-07',
#                                      endDate='2020-08-07')