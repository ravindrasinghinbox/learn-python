# create a parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printName(self):
        print(self.firstname, self.lastname)
x = Person("Jhon", "Deo")
x.printName()
# child class
class Student(Person):
    pass
x = Student("make", "it easy")
x.printName()
# __init__()
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)

# add __init function to student
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname,lname)

s = Student("Ok", "fine")
s.printName()
# add properties
class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.gYear = year
s = Student("Ok", "fine",2018)
s.printName()
# add methods
class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.gYear = year
    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"To the class of ",self.gYear)
s = Student("Ok", "fine",2018)
s.welcome()