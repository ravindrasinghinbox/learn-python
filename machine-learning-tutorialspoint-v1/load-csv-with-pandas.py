from pandas import read_csv
import os

path = os.path.dirname(__file__) + '/data/iris.csv'
data = read_csv(path)
print(data.shape)
print(data)

path = os.path.dirname(__file__) + '/data/pima-indians-diabetes.csv'
headers = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path,names=headers)
print(data.shape)
print(data)