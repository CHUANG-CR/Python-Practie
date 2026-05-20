# 載入 numpy 模組
import numpy as np
# 載入 pandas 模組
import pandas as pd

# 讀入 read.csv 檔案
data = pd.read_csv("read.csv") 
arr = data.values

print(f"資料型態 ：{type(arr)}")
print(f"平均值 ：{arr.mean() :.2f}")
print(f"中位數 ：{np.median(arr) :.2f}")
print(f"標準差 ：{arr.std() :.2f}")
print(f"變異數 ：{arr.var() :.2f}")
print(f"極差值 ：{arr.max()-arr.min() :.2f}")

# 載入 numpy 模組
import numpy as np
# 載入 pandas 模組
import pandas as pd

# 讀入 read.csv 檔案
data = pd.read_csv("read.csv") 
arr = data.values

print('資料型態：%s' % type(arr))
# 計算平均數
print('平均值：%.2f' % np.mean(arr))
# 計算中位數
print('中位數：%.2f' % np.median(arr))
# 計算標準差
print('標準差：%.2f' % np.std(arr))
# 計算變異數
print('變異數：%.2f' % np.var(arr))
# 計算極差值
print('極差值：%.2f' % (np.max(arr) - np.min(arr)))
