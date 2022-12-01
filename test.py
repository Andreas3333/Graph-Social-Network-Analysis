import pandas as pd
from dtwParallel import dtw_functions
from scipy.spatial import distance as d
import numpy as np
'''
get all values of name column and store in series object,
reduce series object to contain single instances of the name value called (name_arr),
then 
use name_arr to select rows based on column
create new dataframes containing only rows of unique 'name' attribute
////////////////////////////////////////////
Data cleaning code-

df = pd.read_csv('final_Dataset.csv', sep=',', lineterminator='\n')
df.drop(columns=["Unnamed: 0", "High", "Low", "Close", "Adj Close"], inplace=True)
df.convert_dtypes(convert_string=True)
print(df.info())

f = open("basic_stock_dataset.csv", "w")
str = str(df)
f.write(str)
f.close()
////////////////////////////////////////////


df = pd.read_csv('final_Dataset.csv', sep=',', lineterminator='\n')
i = 4
while i >= 0:
    name_arr = df.get('Sector' == 'Technology') #get() returns pandas.Series obj, array containing all company names in dataset

    name_arr = name_arr.drop_duplicates(inplace = True) #inplace ensures a new obj is not returned, rather duplicate values are removed on the passed obj 
    i -= 1
print(name_arr.to_string())


for i in name_arr:

    print(i)

    #company = df[df['Name'] == i]
    
    #f = open('datasets/%s.csv' % i, 'w')
    
    name_arr.to_csv('datasets/%s.csv' % i)
    
    fill = company.to_string() #change df type obj to str, only string type data can be written to file
    f.write(fill)
    f.close()

df = pd.read_csv('final_Dataset.csv', sep=',', lineterminator='\n')
 
company = df[df["Sector"] == "Information Technology"]

infoTechSector_name_arr = company.get("Name")

infoTechSector_name_arr.drop_duplicates(inplace = True)

itr = 0
for i in infoTechSector_name_arr:
    indivComp = company[company["Name"] == i]

    indivComp.to_csv("datasets/%s.csv" % i, sep=",")
    itr += 1
    if itr >= 5:
        break

print('Done')


class Input:
    def __init__(self):
        self.check_errors = False 
        self.type_dtw = "i"
        self.MTS = False
        self.n_threads = -1
        self.distance = "dtw"
        self.visualization = False
        self.output_file = False
        self.DTW_to_kernel = False
        self.sigma_kernel = 1

input_obj = Input()


df_1 = pd.read_csv('datasets/Accenture.csv', sep=',')
df_2 = pd.read_csv('datasets/Adobe.csv', sep=',', lineterminator='\r')
df_3 = pd.read_csv('datasets/AdvancedMicroDevices.csv', sep=',', lineterminator='\r')
df_4 = pd.read_csv('datasets/AkamaiTechnologies.csv', sep=',', lineterminator='\r')
df_5 = pd.read_csv('datasets/Amphenol.csv', sep=',', lineterminator='\r')

#attributes = df_1.head(0) #list of data file attributes

open_1 = np.array(df_1.Open.to_numpy(dtype=int), ndmin=1)
open_2 = np.array(df_2.Open.to_numpy(dtype=int), ndmin=1)
open_3 = np.array(df_3.Open.to_numpy(dtype=int), ndmin=1)
open_4 = np.array(df_4.Open.to_numpy(dtype=int), ndmin=1)
open_5 = np.array(df_5.Open.to_numpy(dtype=int), ndmin=1)


#print(open_1.shape[1])

data_list = [open_1, open_2, open_3, open_4, open_5]
distance_metric = d.euclidean

for x in data_list:
    for y in data_list:
        
'''
#distance = d.euclidean
#list_1=[1,2,3]
#list_2=[0,0,1]
      
# API call. 
#dist_matrix = np.array(dtw_functions.dtw(list_1, list_2, dist=distance_metric))
#dtw_functions.dtw(list_1,list_2,distance)

#dtw_functions.dtw(
#agregate distance arrays of companies in to a distance matrix
#for some threashold-
#transform distance array into adj list
#from adj list create verticie and edge list
from dtwParallel import dtw_functions
from scipy.spatial import distance as d

# For Univariate Time Series
x = [4,2,8,4,5]
y = [0,1,0,8,9]

distance = d.euclidean
visualization=True
_ = dtw_functions.dtw(x,y,distance, get_visualization=visualization)

print('Done')
