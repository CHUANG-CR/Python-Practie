# 載入 requests 與 json 模組
import requests , json

# 開放資料Json格式連結
url = "http://tqc.codejudger.com:3000/target/5205.json"
# 發出Get請求
response = requests.get(url)
# 回傳內容長度
print("Content-Length:",len(response.content))
# 將取得的回傳內容轉換成Json格式
res = json.loads(response.text)

print()

# 顯示新北市每一個地區的PM2.5相關資料
print('新北市PM2.5相關資料：')
for record in res:
    if record['County'] == '新北市':
        print('%s：' % record['SiteName'])
        print('\tAQI：%s' % record['AQI'])
        print('\tPM2.5：%s' % record['PM2.5'])
        print('\tPM10：%s' % record['PM10'])
        print('\t資料更新時間：%s' % record['PublishTime'])

  '''
  OUTPUT

  新北市PM2.5相關資料：
汐止：
	AQI：36
	PM2.5：16
	PM10：36
	資料更新時間：2018-06-27 13:00
萬里：
	AQI：49
	PM2.5：10
	PM10：20
	資料更新時間：2018-06-27 13:00
新店：
	AQI：45
	PM2.5：22
	PM10：22
	資料更新時間：2018-06-27 13:00
土城：
	AQI：60
	PM2.5：20
	PM10：32
	資料更新時間：2018-06-27 13:00
板橋：
	AQI：38
	PM2.5：15
	PM10：42
	資料更新時間：2018-06-27 13:00
新莊：
	AQI：42
	PM2.5：12
	PM10：27
	資料更新時間：2018-06-27 13:00
菜寮：
	AQI：60
	PM2.5：20
	PM10：32
	資料更新時間：2018-06-27 13:00
林口：
	AQI：58
	PM2.5：19
	PM10：27
	資料更新時間：2018-06-27 13:00
淡水：
	AQI：40
	PM2.5：10
	PM10：16
	資料更新時間：2018-06-27 13:00
三重：
	AQI：60
	PM2.5：19
	PM10：62
	資料更新時間：2018-06-27 13:00
永和：
	AQI：50
	PM2.5：21
	PM10：35
	資料更新時間：2018-06-27 13:00
富貴角：
	AQI：42
	PM2.5：
	PM10：11
	資料更新時間：2018-06-27 13:00

  '''
