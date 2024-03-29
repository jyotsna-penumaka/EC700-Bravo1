from csv import reader
from os import path
import json
import pandas as pd 
import csv

i = 0
with open('apiCallsToLetters.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    mapping = list(csv_reader)
    i = i+1

df = pd.read_csv('malware_dataset/malware_API_dataset.csv',header=None,sep='\n') 
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
    missing = []
    
    for i in range (0,rows):
        malware_class = df.iat[i,0].strip('"')
        malware_hash = df.iat[i,1].strip('"')
        malware_syscall = ""
        for j in range (2,cols):
            val = df.iat[i,j]
            if df.iat[i,j] != None:
                val = val.strip('"')
                added = False
                for i in range(0,len(mapping)):
                    if val in mapping[i]:
                        malware_syscall = malware_syscall + mapping[i][0]
                        added = True

                if (added == False):
                    missing.append(val)
                    malware_syscall = malware_syscall + 'a'
        row = [malware_class, malware_hash, malware_syscall]
        csvwriter.writerow(row) 
    
miss = set(missing)
