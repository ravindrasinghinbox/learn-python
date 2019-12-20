print(10>9)
print(bool("abc"))
print(bool(["apple", "cherry", "banana"]))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(0))
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x,int))