# excption handing
try:
    print(x)
except:
    print("An exception occurred")
# many exception
try:
    print(x)
except NameError:
    print("variable x in not defined")
except:
    print("Something else went worng")
# else
try:
    print(1)
except NameError:
    print("variable x in not defined")
except:
    print("Something else went worng")
else:
    print("Nothing went wrong")
# finally
try:
    print(1)
except NameError:
    print("variable x in not defined")
except:
    print("Something else went worng")
else:
    print("Nothing went wrong")
finally:
    print("the try except is finished")
# raise an exception
x = -1
if x < 0:
    # raise Exception("Sorry, No number below zero")
    raise TypeError("Sorry, No number below zero")