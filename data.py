import yfinance as yf

def collect_stocks_data(stocks):
    # Fetch data
    stock_data = yf.download(stocks, start='2019-01-01', end='2024-01-01', interval='1mo')['Adj Close']

    # Calculate returns
    return stock_data.pct_change().dropna()

def collect_stock_data(stock):
    # Fetch data
    stock_data = yf.download(stock, start='2019-01-01', end='2024-01-01', interval='1mo')['Adj Close']

    # Calculate returns
    return stock_data.dropna()

def collect_market_data(market_index):
    # Fetch data
    market_data = yf.download(market_index, start='2019-01-01', end='2024-01-01', interval='1mo')['Adj Close']

    # Calculate returns
    return market_data.pct_change().dropna()