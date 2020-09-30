from scipy import stats
import numpy as np

# speed = [1,1,1,2,2,2]
# speed = [2,2,2,1,1,1]

# # mode will sort data first then it will find first match
# x = stats.mode(speed)

# print(x)

a = np.array([
[6, 8, 3, 0],
[3, 2, 1, 7],
[8, 1, 0, 4],
[5, 3, 0, 5],
[4, 7, 5, 9]
])

# axis 0 will check vertically for example [6,3,8,5,4]
# axis = 0

# axis 1 will check horizental for example [6,8,3,0]
axis = 1
x = stats.mode(a,axis)
print(x)