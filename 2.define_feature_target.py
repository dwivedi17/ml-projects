import pandas as pd

#load the path
path = 'C:\BACKUP\..docs\personal\latest\co-pilot\py\datatrain.csv'

#read the csv file
df = pd.read_csv(path)

#print the columns
print('Printing the columns:')
print(df.columns)

#define the features
#X = df[df.columns]
features = ['LotArea', 'YearBuilt']
X = df[features]

#print the features
print('Printing the features:')
print(X)

#define target
y = df['SalePrice']

#print the target
print('Printing the target:')
print(y)