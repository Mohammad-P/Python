import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
#import six
df= pd.read_csv('.../used_car.csv')
#print(df.shape)
NA_Count = pd.DataFrame({'Sum of NA':df.isnull().sum()}).sort_values(by=['Sum of NA'],ascending=[0])
NA_Count['Percentage'] = NA_Count['Sum of NA']/df.shape[1]
sum(NA_Count['Percentage'])
# 17.1 percent
df['fuel_type']=df['fuel_type'].fillna('Gasoline')# 
df['exterior_color']=df['exterior_color'].fillna('Silver')# fill the missing values in exter.. column with Silver
df['bodystyle']=df['bodystyle'].replace(r'^\s*$', 'Sedan', regex=True) # replace blank rows in bodystyle column with Sedan 
df['trim']=df['trim'].fillna('XLS')
df.fillna(method='ffill',inplace=True)
NA_Count = pd.DataFrame({'Sum of NA':df.isnull().sum()}).sort_values(by=['Sum of NA'],ascending=[0])
NA_Count['Percentage'] = NA_Count['Sum of NA']/df.shape[1]
sum(NA_Count['Percentage'])
#0.0
df["price"]  = df["price"].astype(int) # to change the price values into numbers
df["year"]  = df["year"].astype(int)
df["mileage"]  = df["mileage"].astype(int)
df1=df.drop(['vin'],axis=1) # for privacy purposes, we removed the vin information
df2=df1.iloc[:,1:] # to remove first column
plt.figure(figsize = (12, 8))
##### Plot section
plot = sns.countplot(x = 'make', data = df2)
plt.xticks(rotation = 90)
for p in plot.patches:
    plot.annotate(p.get_height(),
                        (p.get_x() + p.get_width() / 2.0,
                         p.get_height()),
                        ha = 'center',
                        va = 'center',
                        xytext = (0, 5),
                        textcoords = 'offset points')

plt.title("Count of cars based on manufacturers")
plt.xlabel("Manufacturer")
plt.ylabel("Count of cars")
plt.show() # No NULLs
#for label,content in df2.items():	# determine the columns which conatains strings
#   if pd.api.types.is_string_dtype(content):
#        print(label)
# convert string date to categorial data
fuel_cat = df2['fuel_type'].astype('category')
cat_dict = {v:k for k,v in dict(enumerate(fuel_cat.cat.categories)).items()}
df2['fuel_type']=df2['fuel_type'].astype('category').cat.codes
##################
exte_cat=df2['exterior_color'].astype('category')
exte_dict= {v:k for k,v in dict(enumerate(exte_cat.cat.categories)).items()}
df2['exterior_color']=exte_cat.cat.codes
cat_dict.update(exte_dict)
make_cat = df2['make'].astype('category')
make_dict = {v:k for k,v in dict(enumerate(make_cat.cat.categories)).items()}
df2['make']=make_cat.cat.codes
cat_dict.update(make_dict)
model_cat = df2['model'].astype('category')
model_dict = {v:k for k,v in dict(enumerate(model_cat.cat.categories)).items()}
df2['model']=df2['model'].astype('category').cat.codes
cat_dict.update(model_dict)
trim_cat = df2['trim'].astype('category')
trim_dict = {v:k for k,v in dict(enumerate(trim_cat.cat.categories)).items()}
cat_dict.update(trim_dict)
df2['trim']=df2['trim'].astype('category').cat.codes


df2=df2[['make','model','year','mileage','fuel_type','trim','exterior_color','price']]

X_train, X_test, y_train, y_test = train_test_split(df2.iloc[:, :-1], 
                                                    df2.iloc[:, -1], 
                                                    test_size = 0.2, 
                                                    random_state = 42)
standardScaler = StandardScaler()
standardScaler.fit(X_train)
X_train = standardScaler.transform(X_train)
X_test = standardScaler.transform(X_test)

rf = RandomForestRegressor(n_estimators = 100)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
r2_score(y_test, y_pred)
# input data as a list of strings
raw_data=['Nissan','Xterra','2009','31063','Gasoline','Base','Silver']
mapped_data=[*map(cat_dict.get, raw_data)]
data=mapped_data[:2]+raw_data[2:4] +mapped_data[4:]
data=[ int(item) for item in data]
df_in=pd.DataFrame(np.array(data).reshape(1,7),columns=['make','model','year','mileage','fuel_type','trim','exterior_color'])

y_pred = rf.predict(df_in)
print(y_pred)