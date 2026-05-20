import codecs
from bs4 import BeautifulSoup
import pandas as pd
Q,W = [],[]

f = codecs.open("read.html",'r')
soup = BeautifulSoup(f.read(),"html.parser")
table = soup.find_all("div", class_ = "Body")
table2 = table[0].find_all("tr")

for line in table2:
    #print(line.text.split("\n"))
    Q.append(line.text.split("\n")[1])
    W.append(line.text.split("\n")[2])
    
df = pd.DataFrame([Q,W]).T
df.to_csv('write.csv', header =False, index =False, encoding='UTF-8')
df
