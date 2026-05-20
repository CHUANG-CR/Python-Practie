import sqlite3
conn = sqlite3.connect("read.db")

c = conn.cursor()

data = c.execute("SELECT * FROM Employee")

for i in data.fetchall():
    print(i)
'''
OUTPUT:

(1, '小陳', 1997, '新北市', 58000)
(2, '小范', 2000, '臺北市', 50000)
(3, '小施', 1999, '高雄市', 47000)
(4, '小吳', 1998, '台中市', 52000)

'''
