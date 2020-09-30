import pandas
from sklearn import linear_model

df = pandas.read_csv("C:/xampp/htdocs/learn-python/ml/cars.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
# regr.fit(X, y,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
regr.fit(X, y)
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
# coefficient
# print(regr.coef_)
'''
Weight: 0.00755095
Volume: 0.00780526

These values tells us that if the weight increases by 1g, the CO2 emission increases by 0.00755095g.

And if the engine size (Volume) increases by 1 ccm, the CO2 emission increases by 0.00780526 g.
'''

# predictedCO2 = regr.predict([[3300, 1300]])
# print(predictedCO2)