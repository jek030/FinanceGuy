from tiingo import TiingoClient
import numpy as np
import pandas as pd
from io import StringIO
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

eight_stocks = ["AAPL","GOOGL","MSFT", "AMD", "PYPL","SQ", "TSLA","TMXLF"]

frame = []

for ticker in eight_stocks:
    jsonData = client.get_ticker_price(ticker, fmt='json', startDate='2019-08-07',  frequency='daily')
   # print("***************")
   # print(jsonData)
    #here is where u take the difference. each 1st row is the startDate infp and 2nd is the endDate info
    lastYearPrice = 0.0
    thisYearPRice = 0.0
    i =0
    for row in jsonData:
        #print("STOCK: ", ticker,  row['close'])
        if i == 0:
            lastYearPrice = row['close']
        
        thisYearPRice = row['close']
        i += 1
     #% return formula here
    percentReturn = (thisYearPRice / lastYearPrice) * 100
  
    singleStockDataFrame = pd.DataFrame({'Ticker': [ticker], '% Return': [percentReturn]} )
    frame.append(singleStockDataFrame)
    #print()  

YTD_df = pd.concat(frame)

YTD_df = YTD_df.sort_values(by= ['% Return'], ignore_index=True, ascending=False)
# turn data frame to html text
YTD_df.to_html('index.html')
print(YTD_df)


#ticker_history = client.get_dataframe(eight_stocks,
#                                      frequency='daily',
##                                      metric_name='close',
#                                      startDate='2019-08-07',
#                                      endDate='2020-08-07')

