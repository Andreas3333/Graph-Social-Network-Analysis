import pandas as pd
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



df = pd.read_csv('final_Dataset.c`sv', sep=',', lineterminator='\n')

name_arr = df.get('Name') #get() returns pandas.Series obj

name_arr.drop_duplicates(inplace = True) #inplace ensures a new obj is not returned, rather duplicate values are removed on the passed obj 

i = 0
j = name_arr.size
while j >= 0:
    print(i)
    str_1 = str(name_arr[i])
    company = df.query("Courses == str_1")
    #company = df[df['Name'] == name_arr[i]]
    if(i == 1):
        print(i)
    f = open('datasets/%s.csv' % name_arr[i], 'w')
    str = company.to_string() #change df type obj to str, only string type data can be written to file
    f.write(str)
    f.close()
    j -= 1
    i += 1
print('Done')