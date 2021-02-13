import csv
import pandas as pd 
from IPython.display import display 
import json
import os.path
from os import path
from zipfile import ZipFile

with ZipFile('malware_dataset.zip', 'r') as zipObj:
   zipObj.extractall()

df = pd.read_csv('malware_dataset/malware_API_dataset.csv',header=None,sep='\n') 
df = df[0].str.split(',', expand=True)
rows = df.shape[0] 
cols = df.shape[1] 
print("rows: " + str(rows))
print("cols: " + str(cols))

if path.exists("apiDict.json"):
    with open('apiDict.json') as json_file: 
        apiDict = json.load(json_file) 
else:
    apiDict = {"first":0}

for i in range (0,rows):
    for j in range (2,cols):
        val = df.iat[i,j]
        if df.iat[i,j] != None:
            val = val.strip('"')
            if val not in apiDict:
                last_key = list(apiDict.keys())[-1]
                apiDict[val] = apiDict[last_key]+1

print(apiDict)
json = json.dumps(apiDict)
f = open("apiDict.json","w")
f.write(json)
f.close()