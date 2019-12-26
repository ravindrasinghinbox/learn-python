import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
# ages = [2, 5, 6, 7, 8, 11, 15, 25, 27, 31, 31, 32, 36, 39, 41, 43, 48, 50, 61, 80, 82]
# # ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# print(np.percentile(ages, 20))
# print(np.percentile(ages, 40))
# print(np.percentile(ages, 60))
# print(np.percentile(ages, 75))
# print(np.percentile(ages, 100))
# # What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.

# # keep diamentios and axis
# a = np.array([
#     [10, 7, 4],
#     [3, 2, 1]
# ])
# # a = [10, 7, 4,3, 2, 1]
# print(np.percentile(a, 50,axis=0,keepdims=True))
# print(np.percentile(a, 50,axis=1,keepdims=True))

# # out
# a = np.array([[10, 7, 4], [3, 2, 1]])
# m = np.percentile(a, 50, axis=0)
# out = np.zeros_like(m)
# np.percentile(a, 50, axis=0, out=out)
# print(m, out)

# # copy
# a = np.array([[10, 7, 4], [3, 2, 1]])
# b = a.copy()
# x = np.percentile(b, 50, axis=1, overwrite_input=True)
# print(x)
# assert not np.all(a == b)


# a = np.arange(4)
# p = np.linspace(0, 100, 200)
# ax = plt.gca()
# print(ax)
# lines = [
#     ('linear', None),
#     ('higher', '--'),
#     ('lower', '--'),
#     ('nearest', '-.'),
#     ('midpoint', '-.'),
# ]
# for interpolation, style in lines:
#     ax.plot(
#         p, np.percentile(a, p, interpolation=interpolation),
#         label=interpolation, linestyle=style)
# ax.set(
#     title='Interpolation methods for list: ' + str(a),
#     xlabel='Percentile',
#     ylabel='List item returned',
#     yticks=a)
# ax.legend()
# plt.show()

# plt.plot([1,2,2,1], [1, 4, 9, 16])
# plt.ylabel('some numbers')
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 10, 0, 20])
# plt.show()

# # evenly sampled time at 200ms intervals
# t = np.arange(1)
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

# data = {'a': np.arange(1,10),
#         'b': [1,5,5,9,5,5,5,1,1],
#         'd': np.arange(1, 10)* 100,
#         'c':['#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
#         }
# cmap = plt.cm.get_cmap("winter")
# cmap.set_under("magenta")
# cmap.set_over("yellow")

# plt.scatter('a', 'b',c='c',s="d",marker='o',alpha=0.5,linewidths=[9,2,5],data=data,plotnonfinite=True,edgecolors='none')
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()

# Plotting with categorical variables

# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]

# plt.figure(figsize=(10,5),dpi=100)

# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()


# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = [1,2,3]
x = [1,2,3]

# plot with various axes scales
plt.figure()

# linear
plt.subplot(111)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True,which='both',color='r', linestyle=':', linewidth=1)

plt.show()