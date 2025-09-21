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

# Student class initializing student attributes
class Student:
    # Data Members
    std_id = 234
    std_name = "Max Deele"
    std_marks = 456
    
    # Member Function
    def show(self):
        print(f"std_id = {self.std_id}")
        print(f"std_name = {self.std_name}")
        print(f"std_marks = {self.std_marks}")
        
obj = Student()
obj.show()

class Marks:
    marks = []
    total = 0
    ave = 0

    def getMarks(self):
        for i in range(5):
            self.marks.append(int(input(f"Enter subject marks {i+1}: ")))
        print(self.marks)
        
    def show_total_ave(self):
        self.total = sum(self.marks)
        print(f"Total = {self.total}")
        self.ave = self.total/5
        print(f"Average = {self.ave}")
            
obj = Marks()
obj.getMarks()
obj.show_total_ave()

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

obj = Student("Max", 24, "A")
obj.display_info()

# Example usage
s1 = Student("Alice", 20, "A")
s1.display_info()

print("\nAccess via getters:")
print("Name:", s1.get_name())
print("Age:", s1.get_age())
print("Grade:", s1.get_grade())
