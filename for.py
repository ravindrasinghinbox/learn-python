# loop in list tuple a dictionary set or string
for x in ["apple","make","sure"]:
    print(x)
# loop in string
for x in "make is easy":
    print(x)
# loop with break
for x in [1, 2, 3, 4, 5]:
    if x == 3:
        break
    print(x)
# continue in loop
for x in [1, 2, 3, 4, 5]:
    if x == 3:
        continue
    print(x)
# range in loop
for x in range(5):
    print(x)
for x in range(2,10,2):
    print(x)
# else in loop
for x in range(2,10,2):
    print(x)
else:
    print("finally finished")
# nested in loop
for x in range(2, 10, 2):
    for i in range(5):
        print(x)
else:
    print("finally finished")
# pass in loop
for x in [1, 2, 3]:
    pass
print("pass get trigger")