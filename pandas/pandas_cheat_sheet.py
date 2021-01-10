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

csv_df = pd.read_csv("sample_data/sample.csv")
print(csv_df)
#   Unnamed: 0  生徒A  生徒B  生徒C
# 0      国語   50     87     76
# 1      数学   82     63     94
# 2      英語   73     59     43