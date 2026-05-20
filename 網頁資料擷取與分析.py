# 引入 pandas 套件，這是一個強大的資料處理與分析套件，並將其簡稱為 pd
import pandas as pd

# 引入 json 套件，用於處理 JSON 格式的資料
import json

# 以「唯讀模式 ('r')」打開名為 'read.json' 的檔案，並指定編碼為 'UTF-8' 以避免讀取中文時出現亂碼
# 將這個檔案物件指派給變數 fp (file pointer)
fp = open('read.json', 'r', encoding='UTF-8')

# 讀取檔案中的所有內容，並將這些文字資料存入變數 a (此時 a 是一個純文字字串)
a = fp.read()

# 使用 json.loads() 函式，將 JSON 格式的字串 (a) 轉換為 Python 可讀取的資料結構 (通常是字典或列表)
# 存入變數 b
b = json.loads(a)

# 利用 pandas 將剛才轉換好的資料 (b) 轉換成 DataFrame (可以想像成 Excel 般的二維表格)
# 存入變數 df
df = pd.DataFrame(b)

# 從完整的表格 df 中，只挑選出 "title"、"showUnit"、"startDate"、"endDate" 這四個特定的欄位
# 將這個過濾後的新表格存入變數 ndf (new DataFrame)
ndf = df[["title", "showUnit", "startDate", "endDate"]]

# 將過濾後的新表格 ndf 匯出並存成名為 'write.csv' 的 CSV 檔案
# header=False 代表匯出的檔案不包含欄位名稱 (表頭)
# index=False 代表匯出的檔案不包含最左邊的資料列索引號碼 (0, 1, 2...)
# encoding='UTF-8' 確保匯出的檔案在顯示中文時不會變成亂碼
ndf.to_csv('write.csv', header=False, index=False, encoding='UTF-8')

# 從 google.colab 套件中引入 files 模組 (這是 Google Colab 雲端筆記本特有的功能)
from google.colab import files

# 觸發瀏覽器下載動作，將雲端環境中剛剛生成的 'write.csv' 下載到你的個人電腦裡
files.download('write.csv')

# 在程式碼最後單獨寫變數名稱，目的是在 Jupyter Notebook 或 Colab 的介面中，直接印出並預覽 ndf 這個表格的內容
ndf
