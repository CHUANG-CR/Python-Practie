import pandas as pd
import xml.etree.ElementTree as ET
tree = ET.parse('read.xml')
root = tree.getroot()
Q,W,E = [],[],[]

i = 0
for child in root:
    i += 1
    Q.append(root[i-1][0].text)
    W.append(root[i-1][1].text)
    E.append(root[i-1][2].text)
    
df = pd.DataFrame([Q,W,E])
df.T.to_csv('write.csv',header = False ,index=False ,encoding='UTF-8')
df.T

from google.colab import files
files.download('write.csv')
