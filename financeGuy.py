from tiingo import TiingoClient
import numpy as np
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

ticker_metadata = client.get_ticker_metadata("GOOGL")

#print(ticker_metadata)
ticker_history = client.get_dataframe("GOOGL")
#print(ticker_history)

apple = client.get_ticker_price("AAPL", fmt='json', 
startDate='2019-08-07', endDate='2020-08-07', frequency='annually')

google = client.get_ticker_price("GOOGL", fmt='json', 
startDate='2019-08-07', endDate='2020-08-07', frequency='annually')

for row in apple:
    print(row['date'], row['close'])

#historical_prices.to_html('index.html')