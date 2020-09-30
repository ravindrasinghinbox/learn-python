import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

# df = pandas.read_csv("C:/xampp/htdocs/learn-python/ml/cars2.csv")
# X = df[['Weight', 'Volume']]
# scaleX = scale.fit_transform(X)
# print(scaleX)

# predict co2 values
df = pandas.read_csv("C:/xampp/htdocs/learn-python/ml/cars2.csv")
X = df[['Weight', 'Volume']]
y = df[['CO2']]
scaleX = scale.fit_transform(X)
regr = linear_model.LinearRegression()
regr.fit(scaleX, y)

scaled = scale.transform([[2300, 1.3]])
print(scaled)
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)