# create class marks with 3 data members
class Marks:
    sub1 = 0
    sub2 = 0
    sub3 = 0
    def getMarks(self):
        self.sub1 = int(input("Enter marks of subject 1: "))
        self.sub2 = int(input("Enter marks of subject 2: "))
        self.sub3 = int(input("Enter marks of subject 3: "))
    def showMarks(self):
        print("Marks of subject 1: ", self.sub1)
        print("Marks of subject 2: ", self.sub2)
        print("Marks of subject 3: ", self.sub3)
    def total(self):
        print("Total marks: ", self.sub1 + self.sub2 + self.sub3)
    def avg(self):
        print("Average marks: ", (self.sub1 + self.sub2 + self.sub3)/3)
obj = Marks()
obj.getMarks()
obj.showMarks()
obj.total()
obj.avg()


# Class with one integer data member
class Maxx:
    num = 0
    def i_n(self):
        self.num = int(input("Enter a number: "))
    def out(self):
        print("Number is: ", self.num)
obj = Maxx()
obj.i_n()
obj.out()

# Prob 3 = create class, get number from user and display table of that number
class Table:
    num = 0
    def getNum(self):
        self.num = int(input("Enter a number: "))
    def show_table(self):
        for i in range(1, 11):
            print(str(self.num) +" * "+str(i)+" = "+str(self.num*i))
obj = Table()
obj.getNum()
obj.show_table()

# prob 2
lst2 = []
for i in range(5):
    color = input("Enter a color: ")
    lst2.append(color)
print("List is: ", lst2)
c = input("Enter color name to find occurrence: ")
total_num_color = lst2.count(c)
print("Total occurrence of ", c, " is: ", total_num_color)


# Prob 1, create list, pass 2 function and find min and max

lst = []
for i in range(5):
    num = int(input("Enter a number: "))
    lst.append(num)
print("List is: ", lst)
def find_minimum(lst):
    print("Minimum number is: ", min(lst))  
def find_maximum(lst):
    print("Maximum number is: ", max(lst))
    
find_minimum(lst)
find_maximum(lst)
