from fredapi import Fred
import pandas as pd

# more on this here:
# https://github.com/mortada/fredapi

# Set API Key here:
fred = Fred(api_key='c2c4766ab4720a73ce1c3f0bb2e21911')

# Series IDs & start dates:
# 1M UST - DGS1MO - 2001-07-31
# 3M UST - DGS3MO - 1982-01-04
# 6M UST - DGS6MO - 1982-01-04
# 1Y UST - DGS1 - 1962-01-02
# 2Y UST - DGS2 - 1976-06-01
# 3Y UST - DGS3 - 1962-01-02
# 5Y UST - DGS5 - 1962-01-02
# 7Y UST - DGS7 - 1969-07-01
# 10Y UST - DGS10 - 1962-01-02
# 20Y UST - DGS20 - 1993-10-01
# 30Y UST - DGS30 - 1977-02-15


# Use API to retreive data from earliest date with all values:
UST1M = fred.get_series('DGS1MO', observation_start='2001-07-31')
UST3M = fred.get_series('DGS3MO', observation_start='2001-07-31')
UST6M = fred.get_series('DGS6MO', observation_start='2001-07-31')
UST1Y = fred.get_series('DGS1', observation_start='2001-07-31')
UST2Y = fred.get_series('DGS2', observation_start='2001-07-31')
UST3Y = fred.get_series('DGS3', observation_start='2001-07-31')
UST5Y = fred.get_series('DGS5', observation_start='2001-07-31')
UST7Y = fred.get_series('DGS7', observation_start='2001-07-31')
UST10Y = fred.get_series('DGS10', observation_start='2001-07-31')
UST20Y = fred.get_series('DGS20', observation_start='2001-07-31')
UST30Y = fred.get_series('DGS30', observation_start='2001-07-31')

# Create dataframe with all values:
data = pd.DataFrame()
data['Date'] = UST1M.index
data['T1M'] = UST1M.values
data['T3M'] = UST3M.values
data['T6M'] = UST6M.values
data['T1Y'] = UST1Y.values
data['T2Y'] = UST2Y.values
data['T3Y'] = UST3Y.values
data['T5Y'] = UST5Y.values
data['T7Y'] = UST7Y.values
data['T10Y'] = UST10Y.values
data['T20Y'] = UST20Y.values
data['T30Y'] = UST30Y.values

# Remove date entries with missing values:
for index, row in data.iterrows():
    if pd.isna(row['T1M']) == True and pd.isna(row['T3Y']) == True:
        data.drop(index, inplace=True)

data.set_index('Date', inplace=True)

# Export to CSV file:
data.to_csv('api_data.csv')
