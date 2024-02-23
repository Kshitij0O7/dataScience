from data import collect_stocks_data, collect_stock_data, collect_market_data
from stocks import market_index, stocks
import statsmodels.api as sm
import pandas as pd
import numpy as np
# print(returns)

def average(returns):
    # Calculate average returns for each stock
    avg_returns = []
    for column in returns.columns:
        avg_returns.append(returns[column].sum() / len(returns[column]))
    return avg_returns

stock_returns = collect_stocks_data(stocks)
print(stock_returns)
market_returns = collect_market_data(stocks)
# print(market_returns)
# Assuming 'returns' is already defined
betas = []
stock_data = collect_stock_data(stocks)
# print(stock_data)

for stock in stocks:
    y = stock_returns[stock]
    X = sm.add_constant(market_returns)
    model = sm.OLS(y, X).fit()
    beta = model.params[1]
    betas.append(beta)

# Store betas with stock symbols
betas_df = pd.DataFrame({'Stock': stock_returns.columns, 'Beta': betas})

# Assuming 'average_returns' is already calculated
average_returns = average(stock_returns)
y = average_returns

X = sm.add_constant(betas_df['Beta'])
model = sm.OLS(y, X)
results = model.fit()

# print(model.summary())

# # Access intercept and slope coefficients
intercept = results.params[0]
slope = results.params[1]
