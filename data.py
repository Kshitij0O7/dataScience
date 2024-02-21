import yfinance as yf

# Define stock symbols
stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS']  # Add all BSE stock symbols

# Fetch data
data = yf.download(stocks, start='2019-01-01', end='2024-01-01')['Adj Close']

missing_values = data.isnull().sum()

# Handle missing values
data = data.dropna()

# Calculate returns
returns = data.pct_change().dropna()
