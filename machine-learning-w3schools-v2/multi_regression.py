import pandas
import os
from sklearn import linear_model


df = pandas.read_csv(os.getcwd()+"/machine-learning/"+"cars.csv")
# print(df)
# s = "a\s"
# s = s.replace("\\","/")
# s = os.path.normpath('.')
# print(os.getcwd())

X = df[['Weight', 'Volume']] 
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)