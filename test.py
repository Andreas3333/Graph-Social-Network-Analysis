import pandas as pd
#import dtw
#from scipy import cluster as cl

'''
get all values of name column and store in series object,
reduce series object to contain single instances of the name value called (name_arr),
then 
use name_arr to select rows based on column
create new dataframes containing only rows of unique 'name' attribute


df.drop(columns=["Unnamed: 0", "High", "Low", "Close", "Adj Close"], inplace=True)
df.convert_dtypes(convert_string=True)
print(df.info())

f = open("basic_stock_dataset.csv", "w")
str = str(df)
f.write(str)
'''



df = pd.read_csv('final_Dataset.csv', sep=',', lineterminator='\n')

name_arr = df.get('Name') #get() returns pandas.Series obj, array containing all company names in dataset

name_arr.drop_duplicates(inplace = True) #inplace ensures a new obj is not returned, rather duplicate values are removed on the passed obj 

i = 0
j = name_arr.size
while j >= 0:
    print(i)
    str_1 = name_arr[i].to_string()
    print(str_1)
    
    #company = df.query('Name == str_1', inplace=False) #inplace=False: do not make changes to original dataframe(default behavior)
    
    company = df[df['Name'] == str_1]
    
    f = open('datasets/%s.csv' % str_1, 'w')
    fill = company.to_string() #change df type obj to str, only string type data can be written to file
    f.write(fill)
    f.close()
    j -= 1
    i += 1 
print('Done')