import numpy as np

# numpy配列を引数に受け取り、値として返却
def fn(x):
    return x * 2

a = np.array([1,2,3])
b = fn(a)
print(b)

# 簡単な計算は標準APIを使う
print(np.sum(a))
print(np.average(a)) # floatが返る
print(np.max(a))
print(np.min(a))