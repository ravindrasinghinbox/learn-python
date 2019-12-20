# syntax
# x = lambda a: a + 10
# print(x(5))
# anonmos functions
def myfun(n):
    return lambda a: a * n
mydoubler = myfun(2)
print(mydoubler(2))
