import pandas as pd
from sklearn.impute import SimpleImputer

#load the path
path = 'C:\BACKUP\..docs\personal\latest\co-pilot\py\datatrain.csv'

#read the file
df = pd.read_csv(path)

#print complete data
print('Printing complete data:')
print(df)

#filter the columns having null values
df_ = df.isna().any()

#print filtered columns
print('Printing filtered columns:')
print(df_)

#define features
X = df[['LotFrontage']]

#print features
print('Printing features:')
print(X)

#define target
y = df['SalePrice']

#print target
print('Printing target:')
print(y)

#Perfrom imputing on selected feature
imputer = SimpleImputer()
imputed_X = imputer.fit_transform(X)
imputed_df = pd.DataFrame(imputed_X, columns = imputer.get_feature_names_out(['LotFrontage']))

#print imputed feature
print('Printing imputed features:')
print(imputed_df)



