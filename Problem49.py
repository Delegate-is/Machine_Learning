# Get hour from user and convert to seconds

h = int(input("Enter hour: "))
s = h*3600
seconds = int(input("Enter seconds: "))
hour = seconds/3600
print(str(hour))
print("You entered "+str(h)+"H")
print(str(h)+" hours is converted to "+str(s)+"seconds")