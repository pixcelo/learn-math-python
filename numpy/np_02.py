import numpy as np

# 要素へのアクセス
a = np.array([1,2,3,4,5])

# インデックス番号を指定
print(a[3]) 

# インデックスを指定して代入
a[3] = 10
print(a[3])

# インデックスを越えて代入
# print(a[5]) # IndexError: index 5 is out of bounds for axis 0 with size 5

# 2次元配列へのアクセス
b = np.array([[0,1,2], [3,4,5]])
# 縦のインデックスが1、横のインデックスが2の要素
print(b[1,2]) # b[1][2]と同じ

# コロンで行や列に対してアクセスできる
print(b[1,:]) # 2行目にアクセス
print(b[:,0]) # 1列目にアクセス