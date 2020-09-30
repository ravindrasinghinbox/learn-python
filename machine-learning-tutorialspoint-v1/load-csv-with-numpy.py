from numpy import loadtxt
import os
path = os.path.dirname(__file__) + '\data\pima-indians-diabetes.csv'
datapath = open(path, 'r')
data = loadtxt(datapath, delimiter=',')
print(data)