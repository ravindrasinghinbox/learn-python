# format
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
txt = "The price is {:.2f} dollars"
print(txt.format(price))
# multiple values
quantity = 3
itemno = 567
price = 49
txt = "I want {} pieces of item number {} for {:.2f} dollars."
print(txt.format(quantity, itemno, price))
# index numbers
txt = "I want {1} pieces of item number {2} for {0:.2f} dollars."
print(txt.format(quantity, itemno, price))
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}"
print(myorder.format(carname="Ford",model = "Mustang"))