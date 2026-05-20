# --開始--批改評分使用，請勿變動
set_seed = 123
# --結束--批改評分使用，請勿變動

import numpy as np

x = np.random.RandomState(set_seed).randint(low=5, high=16, size=15)
print('隨機正整數：', x)

x = x.reshape(3,5)
print('X矩陣內容：')
print(x)
print('最大：',max(np.ravel(x)))
print('最小：',min(np.ravel(x)))
print('總和：',sum(np.ravel(x)))

print('四個角落元素：')
print(x[np.ix_([0, 2], [0, 4])])

'''
OUTPUT

隨機正整數： [ 7  7 11  6  8 15 14 11  6  5  6 14  5  5 14]
X矩陣內容：
[[ 7  7 11  6  8]
 [15 14 11  6  5]
 [ 6 14  5  5 14]]
最大： 15
最小： 5
總和： 134
四個角落元素：
[[ 7  8]
 [ 6 14]]

 '''
