import pandas as pd
import numpy as np
from numpy.random import randn


# Create a panda series
# Understand how values are indexed using labels
# Demostrate how to access the elements from series
# Analyze a few operations on series value
data = np.array(['Mango', 'Banana', 'Apple', 'Pineapple'])
series = pd.Series(data)
print(series)

#adding labels to the series
label = ['a', 'b', 'c', 'd']
series = pd.Series(data, index=label)
print(series)

#Access elements base of label, basically like calling an object
print(series['a'])

#operations on series
series1 = pd.Series([1,2,3,4], ["USA", "Germany", "USSR", "Japan"])
series2 = pd.Series([1,2,5,4], ["USA", "Germany", "Italy", "Japan"])
print(series1 + series2)

# Part 2
# Create Data frames using list
# Create Data frames using dictionary
# Retrieve column values from data frames
# Add a new label and values to data frames
# Fetch rows from dataframes using loc and iloc function
# Fetch value/values from dataframes using row label and column labels
print("####################################################################")
print("Create df using list")
mylist = ['Welcome', 'Data Science', 'World of Analytics', 'V1.0']
df = pd.DataFrame(mylist)
print(df)

print("####################################################################")
print("Create df using dictionary")
data = {
    'Name': ["Jack", "Jill", "Paul"],
    'Age': [24,34,14],
    'Address':['Japan','Australia','Germany'],
    'Department':['IT', 'Buisness', 'Toilet']
}
df = pd.DataFrame(data)
print(df)
print("Indexing and retrieving columns from df..." + df["Name"])
print("Can use the dot notation as well..." + df.Name)
print(df[['Name', 'Age']])

print("####################################################################")
print("Create df using random functions")
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z'])
print(df)
print("adding a new column")
df['New'] = df['X'] + df['Y']
print(df)
print("####################################################################")
print("Tentative drop of a column")
print(df.drop("New", axis=1))
print(df)

print("####################################################################")
print("Selecting rows from dataframes using row indexes or labels")
print(df.loc["C"])
print("Selecting rows based on integer based indexes")
print(df.iloc[2])
print("selecting subset of values from the df")
print(df.loc['A', 'W'])

# Part 3
# Apply operators to dataframes to mine data
# Select/Mine rows of the dataframes
# Select/mine rows of dataframes using complex conditions
# Select/mine columns of df
# Reset col indexes
# Create new col and indexes for df
np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z'])
print("####################################################################")
print("applying comparision operators to df")
print(df>0)
print(df[df>0]) #printing the values instead of t/f, and if below return NaN
print("Displaying all the rows in the df where w is less than 0")
print(df[df['W'] < 0])

print("Display all rows where x is greater than 0 and y is greater than 0, use & and | for 'and' and 'or'")
print(df[(df['X'] > 0) & (df['Z']>0)])
#reset the index, inplace=True will set it to permanent
print(df.reset_index())

newcol = ["KA", "AP", "TN","KL","UP"]
df['States'] = newcol
print(df)
#setting index
print(df.set_index("States"))
#in place attr not assigned true< df index change is temp
print(df)

# Part 4
# Creating a dataframe with NaN
# Drop NaN on row values (Axis = 0)
# Drop Nan on column (Axis = 1)
# Fill NaN values with a prefixed value

print("####################################################################")
d = {
    'A': [1,2,np.nan],
    'B': [5,np.nan, np.nan],
    'C': [1,2,3]
}
df = pd.DataFrame(d)
print(df)
print(df.dropna()) #Drops every row with NaN
print(df.dropna(axis=1)) #Drops every col with NaN
print(df.dropna(thresh=2)) #setting atreshhold on how many NaN
print(df.fillna("Null Values")) #set NaN to Null Values
print(df.fillna(value = df['A'].mean())) #set NaN value in A to the mean of A

# Part 5
# Create df using dict
# Apply group by function to df
# Demostrate aggregate function to a df
# Understand what is describe function in a group by
print("####################################################################")

data = {
    'Company': ['Google', 'Google','Apple', 'FB', 'Apple', 'Microsoft'],
    'Person': ['Jack', 'Jill', 'Dack', 'Bill', 'Zack', 'Back'],
    'Sales': [232, 200, 400, 320, 150, 253]
}
df = pd.DataFrame(data)
print(df)
company_group = df.groupby("Company")
print(company_group)
print(company_group.sum()) #sums up the sales by companies
print(company_group.sum().loc['FB']) #get the value of 'FB'
print(company_group.count())
print(company_group.max()) #displays person name as well, python displays the max string in the person section as well
print(company_group.min())
print(company_group.describe()) #gives a whole description about the group, min max, standard devi
print(company_group.describe().transpose())

# Part 6
# Demostrate inner join
# Apply left outer join
# Understand right outer join
# Apply concat function on axis 0
# Apply concat function on axis 1
print("####################################################################")
print("inner join")
dic1 = {
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2'],
    'index': ['K0', 'K1', 'K2']
}
dic2 = {
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2'],
    'index': ['K0', 'K2', 'K3']
}
left = pd.DataFrame(dic1)
right = pd.DataFrame(dic2)

#Notice where the NaNs are appearing in the different joins
print(pd.merge(left, right, how="inner", on="index"))
print(pd.merge(left, right, how="left", on="index"))
print(pd.merge(left, right, how="right", on="index"))

print(pd.concat([left, right]))
print(pd.concat([left,right], axis=1))

# Part 7
# Create dataframe
# Display unique values of a df
# Apply function to the dataframe col values
# Usage of lambda function in dataframe col
# Create pivot tables using df
print("####################################################################")
df = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2': [232, 444,232, 555],
    'col3': ['abc', 'def', 'ghi', 'jkl']
})
print(df)
print(df['col2'].unique)
print(df['col2'].value_counts())
print(df[(df['col1']>1) & (df['col2'] == 444)])

print("####################################################################")
print("Apply a function to a col of a df")
def times2(x):
    return x*2
print(df['col1'].apply(times2))
print("####################################################################")
print("Apply lambda function to column of a df")
print(df['col2'].apply(lambda x:x*2))
print("####################################################################")
print("display all col names")
print(df.columns)
print(df.sort_values('col2'))
print(df.isnull())

print("####################################################################")
data = {
    'A': ['f','f','f','b','b','b'],
    'B': ['one','one','two','two','two','one'],
    'C': ['x','y','x','y','x','y'],
    'D': [1,3,2,5,4,1]
}
df = pd.DataFrame(data)
print(df)
print("Create a pivot table")
print(df.pivot_table(values='D', index=['A','B']))

# Part 8
# Can read excel sheet
pd.read_excel("sample.xlsx")

#Can put df into excel
pd.to_excel("OutPut.xlsx")
#Read HTML
pd.read_html("sample.html")
# can put into sql tables
from sqlalchemy import create_engine
engine = create_engine("sqlite:///:memory:")
data[0].to_sql("my_table", engine)
sqldf = pd.read_sql("my_table", engine)
sqldf.head(5)