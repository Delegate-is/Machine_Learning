# Python Access Modifier
# Public Modifier -- access attributes or method from anywhere in the program
class Max:
    maxed = 2026
    max_name = "Kevo BB"
    __home = "Kenya"
    
    def showID(self):
        print("Public Python Access Modifier")
        print(self.maxed)
        print(self.max_name)
        
obj = Max()
obj.showID()

# Protected Python Access Modifier== access methods from base and child class in progran(_)

class Student:
    _id = 766
    _name = "Max Dele"
    
    def _show(self):
        print("Protected Python Access Modifier")
        print(f"ID : {self._id}")
        
obj1 = Student()
obj1._show()
        
class Max(Student):
    def ShowDetails(self):
        print(f"Name : {self._name}")
        self._show()
        
obj2 = Max()
obj2.ShowDetails()

#Private Python Access Modifier -- we can only access from base or main class it is declared
class Std:
    _id = 273
    _name = "Max Waz"
    __bd = 2001
    
    def __show(self):
        print("Private Python Access Modifier")
        print(f"Id : {self._id}")
        print(f"Name : {self._name}")
        print(f"Birth Year : {self.__bd}")

    def show(self):     # public method to access private one
        self.__show()
        
obj12 = Std()
obj12.show()

class Waz(Std):
    def ShowDet(self):
        print(f"Name : {self._name}")
        #self.__show()
        
obj3 = Waz()
obj3.ShowDet()

class Mobile:
    mob_number = 34567
    _mob_price = 234323
    _mob_color = "Red"
    mob_model = "Oppo"
class Oppo(Mobile):
    def show(self):
        print("Problem 1: Mobile att")
        print(self._mob_price)
        print(self._mob_color)
        print(self.mob_number)
        print(self.mob_model)
        
obj = Oppo()
obj.show()

# Prob 2: Private Python Access 
class Stds:
    __std_id = 3443
    __std_name = "Max Wpoiru"
    __std_course = "Python OOP"
    
    def _show_info(self):
        print("Prob 2: Private Access")
        print(self.__std_name)
        print(self.__std_id)
        print(self.__std_course)
        
obj = Stds()
obj._show_info()
# Accessing Private members using different approach
class Xyz(Stds):
    def show(self):
        self._show_info()
        
obj = Xyz()
obj.show()

class Car:
    def _set_car_details(self):
        self.__make = input("Enter car make: ")
        self.__model = input("Enter car model: ")
        self.__year = input("Enter car manufacture year: ")
        
    def display_car_details(self):
        print("Car Details")
        print(self.__make)
        print(self.__model)
        print(self.__year)

obj = Car()
obj._set_car_details()
obj.display_car_details()
        

# get alpha char to chec whether it is in a given range or not
import re
# a to f
s = input("Enter a char: ")
x = re.search('[a-fA-F]', s)
if x:
    print("Matching .....")
else:
    print("Not Matching.....")