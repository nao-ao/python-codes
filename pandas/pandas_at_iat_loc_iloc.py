import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.arange(12).reshape(4, 3),
    index = ['A', 'B', 'C', 'D'],
    columns = ['alpha', 'beta', 'gamma']
)
print(df)

#    alpha  beta  gamma
# A      0     1      2
# B      3     4      5
# C      6     7      8
# D      9    10     11

#    alpha  beta  gamma
# A      0     1      2
# B      3     4      5
# C      6     7      8
# D      9    10     11

print(df.at['A', 'alpha'])
# 0
print(df.at['C', 'beta'])
# 7

print(df.iat[0,0])
# 0
print(df.iat[2,1])
# 7

#    alpha  beta  gamma
# A      0     1      2
# B      3     4      5
# C      6     7      8
# D      9    10     11

print(df.loc['B', 'alpha'])
# 3
print(df.iloc[0, 2])
# 2

#    alpha  beta  gamma
# A      0     1      2
# B      3     4      5
# C      6     7      8
# D      9    10     11

print(df.at[df.index[2], 'beta'])
# 7
print(df.at['D', df.columns[2]])
# 11

#    alpha  beta  gamma
# A   1000     1      2
# B      3     4      5
# C      6     7      8
# D      9    10   2000

print(df.loc[ : , 'beta'])
# A     1
# B     4
# C     7
# D    10
# Name: beta, dtype: int64

print(df.iloc[ : , 1])
# A     1
# B     4
# C     7
# D    10
# Name: beta, dtype: int64

#    alpha  beta  gamma
# A   1000     1      2
# B      3     4      5
# C      6     7      8
# D      9    10   2000

print(df.loc['A', :])
# alpha    1000
# beta        1
# gamma       2
# Name: A, dtype: int64

print(df.iloc[1, :])
# alpha    3
# beta     4
# gamma    5
# Name: B, dtype: int64

#    alpha  beta  gamma
# A      0     1      2
# B      3     4      5
# C      6     7      8
# D      9    10     11

# ラベル名で指定する場合
for i in range(len(df)):
  print(df.at[df.index[i], 'beta'])
# 1
# 4
# 7
# 10

# インデックスで指定する場合
for i in range(len(df)):
  print(df.iat[i, 2])
# 2
# 5
# 8
# 11

#    alpha  beta  gamma
# A      0     1      2
# B      3     4      5
# C      6     7      8
# D      9    10     11

# ラベル名で指定する場合
for i in range(len(df.iloc[0,:])):
  print(df.at['D', df.columns[i]])
# 9
# 10
# 11

# インデックスで指定する場合
for i in range(len(df.iloc[0,:])):
  print(df.iat[2, i])
# 6
# 7
# 8
