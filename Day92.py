#   Members in python OOP
# Class is a collection of data member and member function
class Member:
    name = "Max Dele"  #Data Member
    age = 23
    
    def show(self):   #Member Function
        print(self.name)
        print(self.age)
        
obj = Member()
obj.show()