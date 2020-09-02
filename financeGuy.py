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
    #config['api_key'] = "a17ef094e195b4a09409f0fb1753880fc420154a"
    config['api_key'] = "028f16053ce2180643cb2443b4b24736967452c1"



    # Initialize
    client = TiingoClient(config)
    # --START OF OUR CODE--
    top99 = getTickers()
    createLastYearDF(top99, client)
    #create5YearDF(top99, client)
    #create10YearDF(top99, client)

def getTickers():
    top99 =['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOGL', 'GOOG', 'JNJ', 'V', 'PG', 'NVDA', 'HD', 'MA', 'JPM', 'UNH', 'VZ', 'PYPL', 'DIS', 'ADBE', 'MRK', 'NFLX', 'PFE', 'T', 'INTC', 'BAC', 'CMCSA', 'CRM', 'PEP', 'KO', 'WMT', 'ABT', 'CSCO', 'XOM', 'TMO', 'ABBV', 'CVX', 'MCD', 'COST', 'ACN', 'AMGN', 'BMY', 'NKE', 'NEE', 'MDT', 'AVGO', 'UNP', 'LIN', 'DHR', 'QCOM', 'TXN', 'LLY', 'LOW', 'PM', 'ORCL', 'HON', 'UPS', 'IBM', 'AMT', 'C', 'AMD', 'LMT', 'SBUX', 'MMM', 'BA', 'CHTR', 'WFC', 'BLK', 'FIS', 'RTX', 'INTU', 'NOW', 'SPGI', 'GILD', 'CVS', 'MDLZ', 'ISRG', 'MO', 'TGT', 'CAT', 'BKNG', 'ZTS', 'BDX', 'PLD', 'VRTX', 'ANTM', 'EQIX', 'TMUS', 'CCI', 'CL', 'D', 'CI', 'AXP', 'ATVI', 'DE', 'GS', 'TJX', 'APD', 'CME', 'MS', 'REGN']
    #top99 = ['AAPL', 'MSFT', 'PYPL', 'AMZN', 'GOOGL']
    return top99
    


#1
def createLastYearDF(top99, client):
    listOfDFs = [] #a list to temporarily hold each stocks DF so we can combine them
    today = date.today()
    thisYear = today.strftime("%Y")
    lastYear = int(thisYear) - 1
    lastYear = str(lastYear)
    #this is where we get data from JSON - comment out
    ##########
    # for ticker in top99:
    #     jsonData = client.get_ticker_price(ticker, fmt='json', startDate= lastYear+today.strftime('-%m-%d'),  frequency='daily') # gets data fromAPI in JSON format

    #     #here is where u take the difference. each 1st row is the startDate infp0and 2nd is the endDate info
    #     lastYearPrice = 0.0
    #     thisYearPrice = 0.0
    #     i =0
    #     for row in jsonData:
    #         #print("STOCK: ", ticker,  row['close'])
    #         if i == 0:
    #             lastYearPrice = row['close']
            
    #         thisYearPrice = row['close'] #keep iterating until most recent price
    #         i += 1
    #     percentReturn = (thisYearPrice / lastYearPrice) * 100 # percent return formula here
    
    #     singleStockDataFrame = pd.DataFrame({'Ticker': [ticker], '1 Year % Return': [percentReturn]} ) #create a DF of each stock with its ticker and PR
    #     listOfDFs.append(singleStockDataFrame) #append each DF to the list of DFs
    
    # YTD_df = pd.concat(listOfDFs) #Turn list of data frames into one data frame
    # YTD_df = YTD_df.sort_values(by= ['1 Year % Return'], ignore_index=True, ascending=False) #order the DF by highest PR

    #YTD_df.style.format( make_clickable)
    #YTD_df.index = YTD_df.index +1 

    #
   
    
   ########
    # turn data frame to html text

    #new stuff
    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th> what does this do
    html_string = '''
    <link rel="stylesheet" type="text/css" href="df_style.css"/>
    <html>
    <head><title>Top S&P Performers</title>
    <h1> Top S&P Performers </h1>
    </head>
    <body>
        {table}
    <p> Percent return based on stock closing price. </p>
    </body>
    </html>
    '''

    YTD_df = pd.read_csv('YTD.csv', index_col = False)
    YTD_df.drop(YTD_df.columns[0], axis=1, inplace=True) #drops the 2nd column, axis=1 means columns, 0 would be row. inplace means we dont have to reassign the var. 
                                                        #When we read the csv it makes a new col for some reason so we have duplicate indexes
    YTD_df.index = YTD_df.index +1


    #YTD_df.to_csv('YTD.csv')
    print(YTD_df)
    with open('table.html', 'w') as f:
        f.write(html_string.format(table = YTD_df.to_html(classes='mystyle')))


#def make_clickable(val):
            #return '<a target="_blank" href="https://www.tiingo.com/tsla/overview">{}</a>'.format(val,val)



#2
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
    
        singleStockDataFrame = pd.DataFrame({'Ticker': [ticker], '5 Year Return (%)': [percentReturn]} ) #create a DF of each stock with its ticker and PR
        listOfDFs.append(singleStockDataFrame) #append each DF to the list of DFs
    
    YTD_df = pd.concat(listOfDFs) #Turn list of data frames into one data frame
    YTD_df = YTD_df.sort_values(by= ['% Return'], ignore_index=True, ascending=False) #order the DF by highest PR
    print(YTD_df)
    # turn data frame to html text
    YTD_df.to_html('table5.html')   

#3
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
    
        singleStockDataFrame = pd.DataFrame({'Ticker': [ticker], '10 Year Return (%)': [percentReturn]} ) #create a DF of each stock with its ticker and PR
        listOfDFs.append(singleStockDataFrame) #append each DF to the list of DFs
    
    YTD_df = pd.concat(listOfDFs) #Turn list of data frames into one data frame
    YTD_df = YTD_df.sort_values(by= ['% Return'], ignore_index=True, ascending=False) #order the DF by highest PR
    
    print(YTD_df)
    # turn data frame to html text
    YTD_df.to_html('table10.html')


if __name__ == "__main__":
    main()