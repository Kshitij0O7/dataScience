from data import returns
import statsmodels.api as sm
import pandas as pd
import numpy as np
print(returns.dtypes)

def average(returns):
    # Calculate average returns for each stock
    avg_returns = {}
    for column in returns.columns:
        avg_returns[column] = returns[column].sum() / len(returns[column])
    return avg_returns

# Assuming 'market_returns' is already defined
X = sm.add_constant(returns)  # Add intercept
betas = []
# print("Results:")
# print(X.dtypes)
for stock_returns in returns.columns:
    y = returns[stock_returns]
    model = sm.OLS(y, X)
    results = model.fit()
    betas.append(results.params[1])

# Store betas with stock symbols
betas_df = pd.DataFrame({'Stock': returns.columns, 'Beta': betas})

print(betas_df.dtypes)

betas_df = pd.get_dummies(betas_df, columns=['Stock'])

print(betas_df)

# Assuming 'average_returns' is already calculated
average_returns = average(returns)
y = average_returns

# Check data types again
X = sm.add_constant(betas_df)
model = sm.OLS(y, X)
results = model.fit()

# # Access intercept and slope coefficients
intercept = results.params[0]
slope = results.params[1]

print(intercept, slope)
# Perform hypothesis testing (t-test) on intercept and slope
