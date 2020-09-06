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
    config['api_key'] = "a17ef094e195b4a09409f0fb1753880fc420154a"
    #config['api_key'] = "028f16053ce2180643cb2443b4b24736967452c1"



    # Initialize
    client = TiingoClient(config)
    # --START OF OUR CODE--
    SP500 = getTickers()
    #createLastYearDF(top100, client)
    create5YearDF(SP500, client)
    #create10YearDF(top100, client)

def getTickers():
    top100 =['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOGL', 'GOOG', 'BRK-B','JNJ', 'V', 'PG', 'NVDA', 'HD', 'MA', 'JPM', 'UNH', 'VZ', 'PYPL', 'DIS', 'ADBE', 'MRK', 'NFLX', 'PFE', 'T', 'INTC', 'BAC', 'CMCSA', 'CRM', 'PEP', 'KO', 'WMT', 'ABT', 'CSCO', 'XOM', 'TMO', 'ABBV', 'CVX', 'MCD', 'COST', 'ACN', 'AMGN', 'BMY', 'NKE', 'NEE', 'MDT', 'AVGO', 'UNP', 'LIN', 'DHR', 'QCOM', 'TXN', 'LLY', 'LOW', 'PM', 'ORCL', 'HON', 'UPS', 'IBM', 'AMT', 'C', 'AMD', 'LMT', 'SBUX', 'MMM', 'BA', 'CHTR', 'WFC', 'BLK', 'FIS', 'RTX', 'INTU', 'NOW', 'SPGI', 'GILD', 'CVS', 'MDLZ', 'ISRG', 'MO', 'TGT', 'CAT', 'BKNG', 'ZTS', 'BDX', 'PLD', 'VRTX', 'ANTM', 'EQIX', 'TMUS', 'CCI', 'CL', 'D', 'CI', 'AXP', 'ATVI', 'DE', 'GS', 'TJX', 'APD', 'CME', 'MS', 'REGN']
    SP500 = ['MMM','ABT','ABBV','ABMD','ACN','ATVI','ADBE','AMD','AAP','AES','AFL','A','APD','AKAM','ALK','ALB','ARE','ALXN','ALGN','ALLE','LNT','ALL','GOOGL','GOOG','MO','AMZN','AMCR','AEE','AAL','AEP','AXP','AIG','AMT','AWK','AMP','ABC','AME','AMGN','APH','ADI','ANSS','ANTM','AON','AOS','APA','AIV','AAPL','AMAT','APTV','ADM','ANET','AJG','AIZ','T','ATO','ADSK','ADP','AZO','AVB','AVY','BKR','BLL','BAC','BK','BAX','BDX','BRK-B','BBY','BIO','BIIB','BLK','BA','BKNG','BWA','BXP','BSX','BMY','AVGO','BR','BF-B','CHRW','COG','CDNS','CPB','COF','CAH','KMX','CCL','CARR','CAT','CBOE','CBRE','CDW','CE','CNC','CNP','CTL','CERN','CF','SCHW','CHTR','CVX','CMG','CB','CHD','CI','CINF','CTAS','CSCO','C','CFG','CTXS','CLX','CME','CMS','KO','CTSH','CL','CMCSA','CMA','CAG','CXO','COP','ED','STZ','COO','CPRT','GLW','CTVA','COST','COTY','CCI','CSX','CMI','CVS','DHI','DHR','DRI','DVA','DE','DAL','XRAY','DVN','DXCM','FANG','DLR','DFS','DISCA','DISCK','DISH','DG','DLTR','D','DPZ','DOV','DOW','DTE','DUK','DRE','DD','DXC','ETFC','EMN','ETN','EBAY','ECL','EIX','EW','EA','EMR','ETR','EOG','EFX','EQIX','EQR','ESS','EL','EVRG','ES','RE','EXC','EXPE','EXPD','EXR','XOM','FFIV','FB','FAST','FRT','FDX','FIS','FITB','FE','FRC','FISV','FLT','FLIR','FLS','FMC','F','FTNT','FTV','FBHS','FOXA','FOX','BEN','FCX','GPS','GRMN','IT','GD','GE','GIS','GM','GPC','GILD','GL','GPN','GS','GWW','HRB','HAL','HBI','HIG','HAS','HCA','PEAK','HSIC','HSY','HES','HPE','HLT','HFC','HOLX','HD','HON','HRL','HST','HWM','HPQ','HUM','HBAN','HII','IEX','IDXX','INFO','ITW','ILMN','INCY','IR','INTC','ICE','IBM','IP','IPG','IFF','INTU','ISRG','IVZ','IPGP','IQV','IRM','JKHY','J','JBHT','SJM','JNJ','JCI','JPM','JNPR','KSU','K','KEY','KEYS','KMB','KIM','KMI','KLAC','KSS','KHC','KR','LB','LHX','LH','LRCX','LW','LVS','LEG','LDOS','LEN','LLY','LNC','LIN','LYV','LKQ','LMT','L','LOW','LYB','MTB','MRO','MPC','MKTX','MAR','MMC','MLM','MAS','MA','MKC','MXIM','MCD','MCK','MDT','MRK','MET','MTD','MGM','MCHP','MU','MSFT','MAA','MHK','TAP','MDLZ','MNST','MCO','MS','MOS','MSI','MSCI','MYL','NDAQ','NOV','NTAP','NFLX','NWL','NEM','NWSA','NWS','NEE','NLSN','NKE','NI','NBL','NSC','NTRS','NOC','NLOK','NCLH','NRG','NUE','NVDA','NVR','ORLY','OXY','ODFL','OMC','OKE','ORCL','OTIS','PCAR','PKG','PH','PAYX','PAYC','PYPL','PNR','PBCT','PEP','PKI','PRGO','PFE','PM','PSX','PNW','PXD','PNC','PPG','PPL','PFG','PG','PGR','PLD','PRU','PEG','PSA','PHM','PVH','QRVO','PWR','QCOM','DGX','RL','RJF','RTX','O','REG','REGN','RF','RSG','RMD','RHI','ROK','ROL','ROP','ROST','RCL','SPGI','CRM','SBAC','SLB','STX','SEE','SRE','NOW','SHW','SPG','SWKS','SLG','SNA','SO','LUV','SWK','SBUX','STT','STE','SYK','SIVB','SYF','SNPS','SYY','TMUS','TROW','TTWO','TPR','TGT','TEL','FTI','TDY','TFX','TXN','TXT','TMO','TIF','TJX','TSCO','TT','TDG','TRV','TFC','TWTR','TYL','TSN','UDR','ULTA','USB','UAA','UA','UNP','UAL','UNH','UPS','URI','UHS','UNM','VFC','VLO','VAR','VTR','VRSN','VRSK','VZ','VRTX','VIAC','V','VNO','VMC','WRB','WAB','WMT','WBA','DIS','WM','WAT','WEC','WFC','WELL','WST','WDC','WU','WRK','WY','WHR','WMB','WLTW','WYNN','XEL']
    #,'XRX','XLNX','XYL','YUM','ZBRA','ZBH','ZION','ZTS'   ** took this off the end so it's less than 500 calls
   
    #return top100
    return SP500
    


#1
def createLastYearDF(top100, client):
    listOfDFs = [] #a list to temporarily hold each stocks DF so we can combine them
    today = date.today()
    thisYear = today.strftime("%Y")
    lastYear = int(thisYear) - 1
    lastYear = str(lastYear)
    #this is where we get data from JSON - comment out
    ##########
    # for ticker in top100:
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

    
    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th> what does this do
    html_string = '''
    <link rel="stylesheet" type="text/css" href="df_style.css"/>
    <html>
    <head>
    <title>Top S&P Performers</title>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap" rel="stylesheet">
    <h1> Top S&P Performers </h1>
    </head>
    <body>
        {table}
    <p> Percent return is based solely on stock closing price. </p>
    <p> Co-developers: Peter Andresen & James Jelly </p>
    </body>
    </html>
    '''

    YTD_df = pd.read_csv('YTD.csv', index_col = False)
    YTD_df.drop(YTD_df.columns[0], axis=1, inplace=True) #drops the 2nd column, axis=1 means columns, 0 would be row. inplace means we dont have to reassign the var. 
                                                        #When we read the csv it makes a new col for some reason so we have duplicate indexes
    YTD_df.index = YTD_df.index +1


    #YTD_df.to_csv('YTD.csv')
    print(YTD_df)
    # line below adds hyperlink for each ticker, need the escape = false so the html doesn't override
    YTD_df['Ticker']=YTD_df['Ticker'].apply(lambda x: '<a target="_blank" href ="https://finance.yahoo.com/quote/{}">{}</a>'.format(x,x,x))
    #YTD_df.to_html('table.html', escape = False, classes = 'mystyle')
    with open('table.html', 'w') as f:
        f.write(html_string.format(table = YTD_df.to_html(escape = False, classes='mystyle')))



#2
def create5YearDF(SP500, client):
    listOfDFs = [] #a list to temporarily hold each stocks DF so we can combine them
    today = date.today()
    thisYear = today.strftime("%Y")
    lastYear = int(thisYear) - 5
    lastYear = str(lastYear)

    for ticker in SP500:
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
    
    FiveYTD_df = pd.concat(listOfDFs) #Turn list of data frames into one data frame
    FiveYTD_df = FiveYTD_df.sort_values(by= ['5 Year Return (%)'], ignore_index=True, ascending=False) #order the DF by highest PR
    FiveYTD_df.index = FiveYTD_df.index +1

    
    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th> what does this do
    html_string = '''
    <link rel="stylesheet" type="text/css" href="df_style.css"/>
    <html>
    <head>
    <title>Top S&P Performers</title>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap" rel="stylesheet">
    <h1> Top S&P Performers </h1>
    </head>
    <body>
        {table}
    <p> Percent return is based solely on stock closing price. </p>
    <p> Co-developers: Peter Andresen & James Jelly </p>
    </body>
    </html>
    '''
    
    # turn data frame to html text
      
    FiveYTD_df['Ticker']=FiveYTD_df['Ticker'].apply(lambda x: '<a target="_blank" href ="https://finance.yahoo.com/quote/{}">{}</a>'.format(x,x,x))
    with open('table5.html', 'w') as f:
        f.write(html_string.format(table = FiveYTD_df.to_html(escape = False, classes='mystyle'))) 

#3
def create10YearDF(top100, client):
    listOfDFs = [] #a list to temporarily hold each stocks DF so we can combine them
    today = date.today()
    thisYear = today.strftime("%Y")
    lastYear = int(thisYear) - 10
    lastYear = str(lastYear)

    for ticker in top100:
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
    YTD_df = YTD_df.sort_values(by= ['10 Year Return (%)'], ignore_index=True, ascending=False) #order the DF by highest PR
    
    print(YTD_df)
    # turn data frame to html text
    YTD_df.to_html('table10.html')


if __name__ == "__main__":
    main()