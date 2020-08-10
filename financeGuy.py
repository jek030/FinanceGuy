from tiingo import TiingoClient
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