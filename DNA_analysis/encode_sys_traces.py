from os import path
import json
import pandas as pd 
import csv

#df = pd.read_csv('malware_dataset/malware_API_dataset.csv',header=None,sep='\n') 

if path.exists("apiDict.json"):
    with open('apiDict.json') as json_file: 
        apiDict = json.load(json_file) 

df = pd.DataFrame(list(zip(["0"],["0"],["0"])), columns=[])
fields = ['malware_class','malware_hash','malware_syscall']  
filename = "malware_sys_traces.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields) 

    df = pd.read_csv('malware_dataset/malware_API_dataset.csv',header=None,sep='\n') 
    df = df[0].str.split(',', expand=True)
    rows = df.shape[0] 
    cols = df.shape[1] 

    for i in range (0,rows):
        malware_class = df.iat[i,0].strip('"')
        malware_hash = df.iat[i,1].strip('"')
        malware_syscall = ""
        for j in range (2,cols):
            val = df.iat[i,j]
            if df.iat[i,j] != None:
                val = val.strip('"')
                if val not in apiDict:
                    last_key = list(apiDict.keys())[-1]
                    apiDict[val] = apiDict[last_key]+1
                else:
                    malware_syscall = malware_syscall + str(apiDict[val]) + "_"
        row = [malware_class, malware_hash, malware_syscall]
        csvwriter.writerow(row) 



