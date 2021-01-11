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

csv_df = pd.read_csv("sample_data/sample.csv", header=0, names=['教科', '学生A', '学生B', '学生C'])
print(csv_df)
#    教科  学生A  学生B  学生C
# 0  国語   50   87   76
# 1  数学   82   63   94
# 2  英語   73   59   43

csv_df = pd.read_csv("sample_data/sample.csv", index_col=0)
print(csv_df)
#     生徒A  生徒B  生徒C
# 国語   50   87   76
# 数学   82   63   94
# 英語   73   59   43

sample_list = [3,2,4,1,5]
list_to_df = pd.DataFrame(sample_list)
print(list_to_df)
#    0
# 0  3
# 1  2
# 2  4
# 3  1
# 4  5

list_to_ic_df = pd.DataFrame(sample_list, index=['a', 'b', 'c', 'd', 'e'], columns=['column1'])
print(list_to_ic_df)
#    0
# 0  3
# 1  2
# 2  4
# 3  1
# 4  5

sample_2d_list = [[3,2,4,1,5],[30,20,40,10,50],[43,32,42,13,52],]
list_2d_to_df = pd.DataFrame(sample_2d_list)
print(sample_2d_list)
# [[3, 2, 4, 1, 5], [30, 20, 40, 10, 50], [43, 32, 42, 13, 52]]
print(list_2d_to_df)
#     0   1   2   3   4
# 0   3   2   4   1   5
# 1  30  20  40  10  50
# 2  43  32  42  13  52