import pandas as pd
from sklearn.preprocessing import OneHotEncoder

#load the path
path = 'C:\BACKUP\..docs\personal\latest\co-pilot\py\datatrain.csv'

#read the csv file
df = pd.read_csv(path)

#print the complete data
print('Printing complete data:')
print(df)

#select the features: only few which needs to one hot encoded
df_ = df.select_dtypes(include=['object', 'string'])

#print selected columns
print(df_.columns)

#define feature columns
feature_columns = ['SaleType', 'SaleCondition']
X = df[feature_columns]

#print feature
print('Printing feature:')
print(X)

#define target
y = df['SalePrice']

#print target
print('Printing target:')
print(y)

#one hot encoding
ohe  = OneHotEncoder()
encoded_X = ohe.fit_transform(X)
encoded_df = pd.DataFrame(encoded_X.toarray(), columns=ohe.get_feature_names_out(['SaleType', 'SaleCondition']))

#print ohe data
print('Printing ohe data:')
print(encoded_df)

