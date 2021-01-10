import pandas as pd

empty_df = pd.DataFrame()

print(empty_df.empty)
# True

df = pd.DataFrame({
  "名前":['佐藤', '鈴木', '高橋'],
  "年齢":[23, 45, 32],
})

print(df)
#    名前  年齢
# 0  佐藤  23
# 1  鈴木  45
# 2  高橋  32