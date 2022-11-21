import pandas as pd
from dtwParallel import dtw_functions
'''
get all values of name column and store in series object,
reduce series object to contain single instances of the name value called (name_arr),
then 
use name_arr to select rows based on column
create new dataframes containing only rows of unique 'name' attribute


////////////////////////////////////////////
Data cleaning code-

df.drop(columns=["Unnamed: 0", "High", "Low", "Close", "Adj Close"], inplace=True)
df.convert_dtypes(convert_string=True)
print(df.info())

f = open("basic_stock_dataset.csv", "w")
str = str(df)
f.write(str)
////////////////////////////////////////////
'''
'''
df = pd.read_csv('final_Dataset.csv', sep=',', lineterminator='\n')

name_arr = df.get('Name') #get() returns pandas.Series obj, array containing all company names in dataset

name_arr.drop_duplicates(inplace = True) #inplace ensures a new obj is not returned, rather duplicate values are removed on the passed obj 


for i in name_arr:
    print(i)

    company = df[df['Name'] == i]
    
    f = open('datasets/%s.csv' % i, 'w')
    fill = company.to_string() #change df type obj to str, only string type data can be written to file
    f.write(fill)
    f.close()
print('Done')

class Input:
    def __init__(self):
        self.check_errors = False 
        self.type_dtw = "i"
        self.MTS = True
        self.n_threads = -1
        self.distance = "dtw"
        self.visualization = False
        self.output_file = True
        self.DTW_to_kernel = False
        self.sigma_kernel = 1

input_obj = Input()
'''
#restrict data to only first 5 companies of the same sector
#read in csv data files datasets dir
#create df objs of each file
#extract open attribute from df objects and store in arr to send to dtw_ind

company_a = []
company_b = []
for i in df:
    for j in df:
    j += 1
    company_a = df[df['Open'] == i]
    company_b = df[df['Open'] == j]


    f = open('/%s.csv' % i, 'w')
    # API call. 
    dist_arr = dtw_functions.dtw_ind(company_a, company_b, 0, False)


#agregate distance arrays of companies in to a distance matrix
#transform distance array into adj list

print('Done')
