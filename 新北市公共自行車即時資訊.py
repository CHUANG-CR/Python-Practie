# 匯入 pandas 套件，用於資料處理和操作
import pandas as pd
# 匯入 XML 解析模組，用於讀取和處理 XML 檔案
import xml.etree.ElementTree as ET

# 解析 'read.xml' 檔案並獲取 XML 樹狀結構
tree = ET.parse('read.xml')
# 獲取 XML 的根元素
root = tree.getroot()
# 初始化三個空列表，用於儲存從 XML 中提取的資料
Q,W,E = [],[],[]

# 初始化計數器
i = 0
# 逐一遍歷根元素的所有子元素
for child in root:
    # 計數器遞增
    i += 1
    # 從第 i 個子元素的第一個子節點中提取文字內容，儲存到 Q 列表
    Q.append(root[i-1][0].text)
    # 從第 i 個子元素的第二個子節點中提取文字內容，儲存到 W 列表
    W.append(root[i-1][1].text)
    # 從第 i 個子元素的第三個子節點中提取文字內容，儲存到 E 列表
    E.append(root[i-1][2].text)
    
# 使用列表 Q, W, E 建立 DataFrame (資料框)，每一列代表一個列表
df = pd.DataFrame([Q,W,E])
# 將 DataFrame 轉置 (行列互換)，並將結果儲存為 CSV 檔案
# header=False: 不寫入行標題
# index=False: 不寫入行索引
# encoding='UTF-8': 使用 UTF-8 編碼保存，支援中文
df.T.to_csv('write.csv',header = False ,index=False ,encoding='UTF-8')
# 顯示轉置後的 DataFrame 內容
df.T

# 從 Google Colab 匯入檔案下載模組
from google.colab import files
# 下載 'write.csv' 檔案到本地電腦
files.download('write.csv')
