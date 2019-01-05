import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data

df = data.get_data_yahoo('AAPL', '2017-01-01', '2018-01-01')
df.head()

//Check Check
//Check 2
//Check Branch Merge
