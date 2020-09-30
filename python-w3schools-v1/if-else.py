# if
if(2>1):
    print("2 is greater than 1")
# elif
if(5<1):
    print("5 is less than 1")
elif (4 > 2):
    print("4 is greater than 2")
# else
if(5<1):
    print("5 is less than 1")
elif (4 < 2):
    print("4 is less than 2")
else:
    print("No input")
# short hand if
if(4<5):print("4 is greater than 5")
# short hand if else
print("true") if(1<2) else print("false")
# one line if else condition
print("true") if(2<1) else print("true2") if(1<2) else print("false")
# and
if(1<2 and 2<3): print("printing true here")
# or
if(1<2 or 5<3): print("printing true here with or")
# nested if
if (5 < 10):
    print("five is less than 10")
    if (5 < 8):
        print("5 is less than 8")
    else:
        print("greater than 8")
# pass  
if(1<2):pass