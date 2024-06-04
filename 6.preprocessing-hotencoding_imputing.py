import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

#load the path
path = 'C:\BACKUP\..docs\personal\latest\co-pilot\py\datatrain.csv'

#read the csv file
df = pd.read_csv(path)

#print the complete data
print('Printing complete data:')
print(df)

#print head
print('Printing head:')
print(df.head())

#print tail
print('Printing tail:')
print(df.tail())

#print statics
print('Printing desciption:')
print(df.describe())

#print all columns
print('Printing all columns:')
print(df.columns)

#feature selection
feature_columns = ['SaleType','SaleCondition','LotFrontage']
X = df[feature_columns]

#print features
print('Printing features:')
print(X)

#target selection
y = df['SalePrice']

#print target
print('Printing target:')
print(y)

#apply one hot encoding to convert categorical values into numeric in the selected feature
ohe = OneHotEncoder()
#one_hot_candidate = X.select_dtypes(include=['object','string'])
encoded_X = ohe.fit_transform(X)
encoded_df = pd.DataFrame(encoded_X.toarray(), columns = ohe.get_feature_names_out(X.columns))


#print encoded data frame
print('Printing encoded dataframe:')
print(encoded_df)
print(encoded_df.columns)

#apply imputing to encoded_df to further remove null values
myImputer = SimpleImputer()
imputed_X = myImputer.fit_transform(encoded_df)
imputed_df = pd.DataFrame(imputed_X, columns = myImputer.get_feature_names_out(encoded_df.columns))

#print imputed dataset
print('Printing imputed dataset:')
print(imputed_df)



