import pandas as pd

# load the path
path = 'C:\BACKUP\..docs\personal\latest\co-pilot\py\datatrain.csv'

#read the csv file
df = pd.read_csv(path)

#print the file
print('Printing the file:')
print(df)

#print the head
print('Printing the head:')
print(df.head())

#print the head with 8 rows
print('Printing the head with 8 rows:')
print(df.head(8))

#print the tail
print('Printing the tail:')
print(df.tail())

#print the statics
print('Printing the statics:')
print(df.describe())

#print the columns
print('Printing the columns:')
print(df.columns)

