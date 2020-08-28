from tiingo import TiingoClient
from io import StringIO
import numpy as np
import pandas as pd
from datetime import date




def main():
    # Set TIINGO_API_KEY in your environment variables in your .bash_profile, OR
    # pass a dictionary with 'api_key' as a key into the TiingoClient.
    config = {}

    # To reuse the same HTTP Session across API calls (and have better performance), include a session key.
    config['session'] = True

    # If you don't have your API key as an environment variable,
    # pass it in via a configuration dictionary.
    config['api_key'] = "028f16053ce2180643cb2443b4b24736967452c1"


    # Initialize
    client = TiingoClient(config)
    # --START OF OUR CODE--
    top99 = getTickers()
    create5YearDF(top99, client)
    create10YearDF(top99, client)

def getTickers():
    top99 =['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOGL', 'GOOG', 'JNJ', 'V', 'PG', 'NVDA', 'HD', 'MA', 'JPM', 'UNH', 'VZ', 'PYPL', 'DIS', 'ADBE', 'MRK', 'NFLX', 'PFE', 'T', 'INTC', 'BAC', 'CMCSA', 'CRM', 'PEP', 'KO', 'WMT', 'ABT', 'CSCO', 'XOM', 'TMO', 'ABBV', 'CVX', 'MCD', 'COST', 'ACN', 'AMGN', 'BMY', 'NKE', 'NEE', 'MDT', 'AVGO', 'UNP', 'LIN', 'DHR', 'QCOM', 'TXN', 'LLY', 'LOW', 'PM', 'ORCL', 'HON', 'UPS', 'IBM', 'AMT', 'C', 'AMD', 'LMT', 'SBUX', 'MMM', 'BA', 'CHTR', 'WFC', 'BLK', 'FIS', 'RTX', 'INTU', 'NOW', 'SPGI', 'GILD', 'CVS', 'MDLZ', 'ISRG', 'MO', 'TGT', 'CAT', 'BKNG', 'ZTS', 'BDX', 'PLD', 'VRTX', 'ANTM', 'EQIX', 'TMUS', 'CCI', 'CL', 'D', 'CI', 'AXP', 'ATVI', 'DE', 'GS', 'TJX', 'APD', 'CME', 'MS', 'REGN']
    #top99 = ['AAPL', 'MSFT', 'PYPL', 'AMZN', 'GOOGL']
    return top99
    #allTickers = pd.read_csv('nasdaqCSV.csv')

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



def createLastYearDF(top99, client):
    listOfDFs = [] #a list to temporarily hold each stocks DF so we can combine them
    today = date.today()
    thisYear = today.strftime("%Y")
    lastYear = int(thisYear) - 1
    lastYear = str(lastYear)

    for ticker in top99:
        jsonData = client.get_ticker_price(ticker, fmt='json', startDate= lastYear+today.strftime('-%m-%d'),  frequency='daily') # gets data fromAPI in JSON format

        #here is where u take the difference. each 1st row is the startDate infp0and 2nd is the endDate info
        lastYearPrice = 0.0
        thisYearPrice = 0.0
        i =0
        for row in jsonData:
            #print("STOCK: ", ticker,  row['close'])
            if i == 0:
                lastYearPrice = row['close']
            
            thisYearPrice = row['close'] #keep iterating until most recent price
            i += 1
        percentReturn = (thisYearPrice / lastYearPrice) * 100 # percent return formula here
    
        singleStockDataFrame = pd.DataFrame({'Ticker': [ticker], '% Return': [percentReturn]} ) #create a DF of each stock with its ticker and PR
        listOfDFs.append(singleStockDataFrame) #append each DF to the list of DFs
    
    YTD_df = pd.concat(listOfDFs) #Turn list of data frames into one data frame
    YTD_df = YTD_df.sort_values(by= ['% Return'], ignore_index=True, ascending=False) #order the DF by highest PR
    print(YTD_df)
    # turn data frame to html text
    YTD_df.to_html('table.html')

def create5YearDF(top99, client):
    listOfDFs = [] #a list to temporarily hold each stocks DF so we can combine them
    today = date.today()
    thisYear = today.strftime("%Y")
    lastYear = int(thisYear) - 5
    lastYear = str(lastYear)

    for ticker in top99:
        jsonData = client.get_ticker_price(ticker, fmt='json', startDate= lastYear+today.strftime('-%m-%d'),  frequency='daily') # gets data fromAPI in JSON format

        #here is where u take the difference. each 1st row is the startDate infp0and 2nd is the endDate info
        lastYearPrice = 0.0
        thisYearPrice = 0.0
        i =0
        for row in jsonData:
            #print("STOCK: ", ticker,  row['close'])
            if i == 0:
                lastYearPrice = row['close']
            
            thisYearPrice = row['close'] #keep iterating until most recent price
            i += 1
        percentReturn = (thisYearPrice / lastYearPrice) * 100 # percent return formula here
    
        singleStockDataFrame = pd.DataFrame({'Ticker': [ticker], '% Return': [percentReturn]} ) #create a DF of each stock with its ticker and PR
        listOfDFs.append(singleStockDataFrame) #append each DF to the list of DFs
    
    YTD_df = pd.concat(listOfDFs) #Turn list of data frames into one data frame
    YTD_df = YTD_df.sort_values(by= ['% Return'], ignore_index=True, ascending=False) #order the DF by highest PR
    print(YTD_df)
    # turn data frame to html text
    YTD_df.to_html('table5.html')   

def create10YearDF(top99, client):
    listOfDFs = [] #a list to temporarily hold each stocks DF so we can combine them
    today = date.today()
    thisYear = today.strftime("%Y")
    lastYear = int(thisYear) - 10
    lastYear = str(lastYear)

    for ticker in top99:
        jsonData = client.get_ticker_price(ticker, fmt='json', startDate= lastYear+today.strftime('-%m-%d'),  frequency='daily') # gets data fromAPI in JSON format

        #here is where u take the difference. each 1st row is the startDate infp0and 2nd is the endDate info
        lastYearPrice = 0.0
        thisYearPrice = 0.0
        i =0
        for row in jsonData:
            #print("STOCK: ", ticker,  row['close'])
            if i == 0:
                lastYearPrice = row['close']
            
            thisYearPrice = row['close'] #keep iterating until most recent price
            i += 1
        percentReturn = (thisYearPrice / lastYearPrice) * 100 # percent return formula here
    
        singleStockDataFrame = pd.DataFrame({'Ticker': [ticker], '% Return': [percentReturn]} ) #create a DF of each stock with its ticker and PR
        listOfDFs.append(singleStockDataFrame) #append each DF to the list of DFs
    
    YTD_df = pd.concat(listOfDFs) #Turn list of data frames into one data frame
    YTD_df = YTD_df.sort_values(by= ['% Return'], ignore_index=True, ascending=False) #order the DF by highest PR
    print(YTD_df)
    # turn data frame to html text
    YTD_df.to_html('table10.html')


if __name__ == "__main__":
    main()