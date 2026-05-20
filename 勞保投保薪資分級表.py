import sys, json, yaml

with open('read (1).json','r',encoding='UTF-8') as file:
    data = json.load(file) # json.load stands for file path
    
with open("write.yaml",'w', encoding='UTF-8') as f:
    yaml.dump(data,f, default_flow_style = False, allow_unicode=True)
