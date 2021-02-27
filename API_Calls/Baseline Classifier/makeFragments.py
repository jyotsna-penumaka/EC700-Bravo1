import pandas
import csv

csv_data = pandas.read_csv('api_calls.csv')
benign = csv_data[csv_data['malware'] == 0].reset_index(drop=True)
malware = csv_data[csv_data['malware'] == 1].reset_index(drop=True)
malware = malware.drop(malware.index[len(benign):len(malware)])
benign = benign.drop(['hash'], axis=1)
malware = malware.drop(['hash'], axis=1)
data = (pandas.concat([benign,malware])).reset_index(drop=True)
Y = (data['malware'].values).tolist()
data = data.drop(['malware'], axis=1)
data = (data.values).tolist()
data_frag = []
Y_frag = []
for i in range (0,len(data)):
    j = 0
    while (10+j) <= len(data[i]) :
        benign_pattern = data[i][j:(10+j)]
        malware_pattern = data[i][j:(10+j)]
        if ((benign_pattern.append(0) not in data_frag) & (malware_pattern.append(1) not in data_frag)) :
            frag = data[i][j:(10+j)]
            frag.append(Y[i])
            data_frag.append(frag)
            j = j + 1

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data_frag)