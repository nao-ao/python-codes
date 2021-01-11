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

df = pd.read_csv("sample_data/sample.csv")

print(df)
#   Unnamed: 0  生徒A  生徒B  生徒C
# 0      国語   50     87     76
# 1      数学   82     63     94
# 2      英語   73     59     43

df = pd.read_csv("sample_data/sample.csv", header=0, names=['教科', '学生A', '学生B', '学生C'])

print(df)
#    教科  学生A  学生B  学生C
# 0  国語   50   87   76
# 1  数学   82   63   94
# 2  英語   73   59   43

df = pd.read_csv("sample_data/sample.csv", index_col=0)

print(df)
#     生徒A  生徒B  生徒C
# 国語   50   87   76
# 数学   82   63   94
# 英語   73   59   43

sample_list = [3,2,4,1,5]
df = pd.DataFrame(sample_list)

print(df)
#    0
# 0  3
# 1  2
# 2  4
# 3  1
# 4  5

df = pd.DataFrame(sample_list, index=['a', 'b', 'c', 'd', 'e'], columns=['column1'])

print(df)
#    column1
# a        3
# b        2
# c        4
# d        1
# e        5

sample_2d_list = [[3,2,4,1,5],[30,20,40,10,50],[43,32,42,13,52],]
df = pd.DataFrame(sample_2d_list)

print(sample_2d_list)
# [[3, 2, 4, 1, 5], [30, 20, 40, 10, 50], [43, 32, 42, 13, 52]]

print(df)
#     0   1   2   3   4
# 0   3   2   4   1   5
# 1  30  20  40  10  50
# 2  43  32  42  13  52

sample_2d_list = [[3,2,4,1,5],[30,20,40,10,50],[43,32,42,13,52],]
df = pd.DataFrame(sample_2d_list, index=['番号', '国語', '算数'], columns=['生徒A','生徒B','生徒C','生徒D','生徒E'])

print(df)
#     生徒A  生徒B  生徒C  生徒D  生徒E
# 番号    3    2    4    1    5
# 国語   30   20   40   10   50
# 算数   43   32   42   13   52

########################################################################################## 

import numpy as np

numpy_ndarray = np.array([1, 2, 3])

print(numpy_ndarray)
# [1 2 3]

print(type(numpy_ndarray))
# <class 'numpy.ndarray'>

df = pd.DataFrame(numpy_ndarray)

print(df)
#    0
# 0  1
# 1  2
# 2  3

df = pd.DataFrame(numpy_ndarray, index=['a', 'b', 'c'], columns=['column1'])

print(df)
#    column1
# a        1
# b        2
# c        3

numpy_ndarray2 = np.array([[5, 2], [3, 6]])

print(numpy_ndarray2)
# [[5 2]
#  [3 6]]

print(type(numpy_ndarray2))
# <class 'numpy.ndarray'>

df = pd.DataFrame(numpy_ndarray2)

print(df)
#    0  1
# 0  5  2
# 1  3  6

df = pd.DataFrame(numpy_ndarray2, index=['x1', 'x2'], columns=['y1', 'y2'])

print(df)
#     y1  y2
# x1   5   2
# x2   3   6

########################################################################################## 

df = pd.read_csv("sample_data/tests2.csv")

print(df)
#      番号  名前   合計  国語  数学  英語
# 0  A422  佐藤  208  66  88  54
# 1  A114  鈴木  158  42  85  31
# 2  A492  高橋  234  97  98  39
# 3  A444  田中  234  57  90  87
# 4  A198  伊藤  213  78  43  92
# 5  A471  渡辺  202  48  86  68
# 6  A407  山本  215  77  62  76
# 7  A322  中村  263  82  92  89
# 8  A387  小林  168  37  86  45
# 9  A147  加藤  216  90  47  79

print(df['合計'] > 230)
# 0    False
# 1    False
# 2     True
# 3     True
# 4    False
# 5    False
# 6    False
# 7     True
# 8    False
# 9    False

print(df[df['合計'] > 230])
#      番号  名前   合計  国語  数学  英語
# 2  A492  高橋  234  97  98  39
# 3  A444  田中  234  57  90  87
# 7  A322  中村  263  82  92  89
