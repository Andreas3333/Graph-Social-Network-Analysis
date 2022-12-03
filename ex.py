#convert json to csv
import csv
import json
'''
#.txt file to .csv file-
file = pd.read_csv('node_edge.txt', sep=r"\s+", header=None, names=['n', 'm', 'w'], engine="python")

file.to_csv('edge_list.csv', sep=",", index=False)
-------------------------------------------------
#a = np.loadtxt('node_edge.txt')
#a.astype('int64', copy=False)
#print(a[0:5, :])
#file.convert_dtypes({'m': 'int64', 'w': 'int64'}).dtypes
#pd.to_numeric(file['m'])
#pd.to_numeric(file['w'])
#file['m'].astype(int, copy=True)
#file['w'].astype(int, copy=True)
#file.to_csv('edge_list.csv', index=False)
output_csv = open('nodes.csv', 'w') #output file
csv_writer = csv.writer(output_csv) #csv writer object
k = input.keys()
csv_writer.writerow(k)
for data in input:
        
    csv_writer.writerow(input.values())
output_csv.close()
'''
import pandas as pd
import numpy as np
#dtype of "CompanyName" == str, dtype of "node_id" == int64

f = open('Nodes.json', 'r')

jdata = pd.json_normalize(f.read())

jdata.columns['CompanyName', 'node_id']

print(jdata.head())
print(jdata.dtypes)
f.close()