import json
import csv

with open("report.json", "r") as read_file:
    data = json.load(read_file)
    calls = data.get("behavior").get("processes")[1].get("calls");
    numberOfCalls = len(calls)
    api_calls = []
    for i in range (0,numberOfCalls) :
        api_calls.append(calls[i].get("api"))

    with open('cuckoo_calls.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(api_calls)

    if path.exists("apiDict.json"):
        with open('apiDict.json') as json_file: 
            apiDict = json.load(json_file) 