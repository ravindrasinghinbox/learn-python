import csv
import numpy as np
import os
path = os.path.dirname(__file__)+'\data\iris.csv'
with open(path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = list(reader)
    data = np.array(data)
    print(headers)
    print(data.shape)