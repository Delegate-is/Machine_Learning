# Get number and display square of previous and next number
import math
num = int(input("Enter a number: "))
print(f"Previous number: {num - 1}, Square: {(num - 1) ** 2}, Sin value: {math.sin(num - 1)}, Cos value: {math.cos(num - 1)}")
print(f"Next number: {num + 1}, Square: {(num + 1) ** 2}, Sin value: {math.sin(num + 1)}, Cos value: {math.cos(num + 1)}")
# Create a class with two variables: name and id
class Person:
    def __init__(self):
        self.name = None
        self.id = None

    def get_Data(self):
        self.name = input("Enter name: ")
        self.id = input("Enter ID: ")

    def show(self):
        print(f"Name: {self.name}, ID: {self.id}")

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}"
obj = Person()
obj.get_Data()
obj.show()
print(obj)  # Print the string representation of the object
# Class to demonstrate inheritance
class Student(Person):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.roll_no = None

    def get_Data(self):
        super().get_Data()  # Get data from the parent class
        self.roll_no = input("Enter Roll No: ")

    def show(self):
        super().show()  # Show data from the parent class
        print(f"Roll No: {self.roll_no}")

    def __str__(self):
        return f"{super().__str__()}, Roll No: {self.roll_no}"