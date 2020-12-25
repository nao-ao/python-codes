import matplotlib.pyplot as plt

# 図の下地
fig = plt.figure()
# figsize パラメータのデフォルト値は[6.4、4.8]

# 図のタイトル
fig.suptitle('title')

# 図の間隔の調整
fig.subplots_adjust(wspace=1.0)

# 図の中に3つのグラフを作成 2×2の1つ目から3つ目まで
# ax = fig.add_subplot(1, 1, 1, xlabel='xlabel', ylabel='ylabel')
ax1 = fig.add_subplot(2, 2, 1, xlabel='xlabel', ylabel='ylabel')
ax2 = fig.add_subplot(2, 2, 2, xlabel='xlabel', ylabel='ylabel')
ax3 = fig.add_subplot(2, 2, 3, xlabel='xlabel', ylabel='ylabel')

# 出力するデータ
x = [1,2,3,4]
y = [3,2,1,0]
z = [10,21,12,14]

# 折れ線
ax1.plot(x, y)
# 散布図
ax2.scatter(x, y)
# 棒グラフ
ax3.bar(x, z)

# 図のレイアウトをコッチで調整することもある。
# fig.tight_layout()

#画像の保存
# 対応している拡張子
# eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff
fig.savefig('file.png')