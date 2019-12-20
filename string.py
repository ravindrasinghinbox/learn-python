# print('Hello')
# print("Hello")

# a = "hello"
# print(a)

# multiline commend with double quotes
# a = """
# This is something about multiple line
# here we go multiple line
# """
# print(a)

# multiline with single quotes
# a = '''this is multiline example with single quote
#     large text goes here'''
# print(a)

# string are array
# a = "this is string array"
# print(a[1])

# slicing
# a = "hello world"
# print(a[0:1])

# a = "Hello, World!"
# print(a[-5:-2])   

# get len of string
# a = "hello world"
# print(len(a))

#strip string
# a = " hello world  "
# print(a.strip())

# string lower
# a = "welcome Make It usual"
# print(a.lower())

# string uppper
# a = "welcome Make It usual"
# print(a.upper())

# string replace
# a = "a a a"
# print(a.replace("a",'A'))

# string split
# a = "Hello,world,goes,here,today"
# a = a.split(",")
# print(a)

# text in string
# a = "Hello you are here "
# x = "yous" in a
# print(x)


# text not in string
# a = "Hello you are here "
# x = "you" not in a
# print(x)

# string concatnet
# a = "hello"
# b = "world"
# c = a +" "+ b
# print(c)

# format string
# a = "this is my {} thank you {}"
# print(a.format('ravindra', 'Per'))


# format string with index
# a = "this is my {1} thank you {0}"
# print(a.format('ravindra','Per'))

# double quote in quote and hexa and octal feed and backslash
# print("\"double quote\"")
# print("\\Backslah")
# print("\nnew line")
# print("\rcarriage return how does it works")
# print("\ttab\ttab")
# print("a \bbackspace")
# print("\fform feed\fform feed")
# print("\100 octal value")
# print("\xff hex value")

# method string
# print("casefold convert more charects when matches more ".casefold())
# print("a".center(10,"*"))
# print("a\tb\tc\td".expandtabs(7))
# print("you can find here".find("y",0,1))
# print("you are here {price:.2f}".format(price=49))
# print("check this format {p:<3} buy".format(p=3))
# print("check this format {p:^3} buy".format(p=3))
# print("check this format {p:=8} buy".format(p=-5))
# print("tempreture is between {:+} and {:+}".format(-3,7))
# print("tempreture is between {:-} and {:-}".format(-3,7))
# print("tempreture is between {:} and {:}".format(-3,7))
# print("Your number goes here {:,} and {:,}".format(1000,500))
# print("the universe is {:_} years old".format(13800000000))
# print("the universe is {:b} years old".format(5))
# print("unicode charecter {:c} years old not getting".format(49))
# print("decmial format {:d}".format(0b101))
# print("decmial format {:e}".format(5))
# print("decmial format {:E}".format(5))
# print("decmial format {:.2f}".format(5))
# print("decmial format {:f}".format(5))
# print("decmial format {:F}".format(float('inf')))
# print("decmial format {:g}".format(5))
# print("decmial format {:G}".format(5))
# print("decmial {0} format {0:o}".format(10))
# print("hex {0} format {0:x}".format(16))
# print("hex {0} format {0:X}".format(255))
# print("hex {0} format {0:%}".format(255))
# print("demo".isidentifier())
# print("Hello! Are you #1".isprintable())
# print("Hello! Ar\ne you #1".isprintable())
# print("OK".isupper())
# print("#".join(("ok","make","easy")))
# print("banana".ljust(20),"is my favorite fruit")
# print("banana".rjust(20),"is my favorite fruit")
# print("I could eat bananas all day".partition("bananas"))
# print("easy ok make it easy".rfind("easy")) 
# print("easy ok make it easy".rjust(20))
# print("i make it easy here to do it easy ".partition("here"))
# print("i make it easy here to do easy it".rpartition("here"))
# print("apple, banana, cherry, make, ok".rsplit(", ",1))
# print("apple, banana, cherry, make, ok".split(", ",))
# print("    banana     ".rstrip())
# print("    banana     ".lstrip())
# print("just make is easy\n and make new line\n".splitlines())
# print("just make is easy\n and make new line\n".splitlines(True))
# print("ok go here ".startswith("ok",4))
print("make is user".swapcase())
print("make is user".swapcase().swapcase())
print("ok goes here".title())
print("hello b2b2b2 and 3g3g3g".title())
print("just make sure".upper())
print("50".zfill(10))