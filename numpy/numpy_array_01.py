import numpy as np

# numpy配列 (1次元)
a = np.array([0,1,2,3,4,5])
print(a)

# numpy配列 (2次元)
b = np.array([[0,1,2,],[3,4,5]])
print(b)

# 配列の形状を調べる (2x3の2次元配列)
print(np.shape(b)) # (2, 3)

# 配列の行数を調べる
print(len(b))

# 0だけの配列
c = np.zeros(8)
print(c)

# 1だけの配列
d = np.ones(8)
print(d)

# 連番の配列
e = np.arange(8)
print(e)

# 配列の演算 (各要素の数値の間で演算が行われる)
print(e + 3) # 各要素に3を足す

# 配列同士の演算
f = np.array([0,1,2,3,4,5])
g = np.array([1,3,5,7,9,11])
print(f)
print(g)
print(f + g)