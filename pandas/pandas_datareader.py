# pip install pandas-datareader
import datetime as dt
from dateutil.relativedelta import relativedelta

import pandas as pd
import pandas_datareader.data as web

# 日付指定（直接）
# end = dt.date(2017,9,16)

# 今日
end = dt.date.today()

# 日付計算
start = end - dt.timedelta(days=1)
start = end - dt.timedelta(weeks=1)
start = end - relativedelta(months=1)
start = end - relativedelta(years=1)

print(start,end)

# 日本株の取得
df = web.DataReader('7203.JP', 'stooq', start, end) 

# 米国株の取得
df = web.DataReader('VYM', 'yahoo', start, end) 

# 配当金の取得（どちらでも可）日本株は無理
df = web.DataReader('SPYD', 'yahoo-actions', start, end) 
df = web.DataReader('SPYD', 'yahoo-dividends', start, end)

# 銘柄の情報 日本株は無理
df = web.get_quote_yahoo('SPYD')
# 得られる情報の一覧
for i in range(len(df.columns)):
  print(df.columns[i] + ' - ' +str(df.iat[0,i]))

df = web.get_quote_yahoo('KO')
# 得られる情報の一覧 ETFと個別株では少し違う
for i in range(len(df.columns)):
  print(df.columns[i] + ' : ' +str(df.iat[0,i]))
  
# ドル円の取得
USDJPY = web.DataReader('DEXJPUS', 'fred', start, end)