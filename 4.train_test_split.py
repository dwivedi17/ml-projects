import pandas as pd
from sklearn.model_selection import train_test_split

#load the path
path = 'C:\BACKUP\..docs\personal\latest\co-pilot\py\datatrain.csv';

#read the csv file
df = pd.read_csv(path)

#print the data
print('Printing complete data:')
print(df)

#print the columns
print('Printing columns:')
print(df.columns)

#define features
feature_columns = ['LotArea', 'YearBuilt']
X = df[feature_columns]

#print features
print('Printing features:')
print(X)

#define target
y = df['SalePrice']

#print target
print('Printing target:')
print(y)

#define training and test data
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)

#print training feature
print('Printing training X:')
print(train_X)

#print testing feature
print('Printing testing X:')
print(test_X)

#print training target
print('Printing training y:')
print(train_y)

#print testing target
print('Printing testing y:')
print(test_y)

