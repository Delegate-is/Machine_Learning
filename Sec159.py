# Program to create an empty class
class MAX:
    pass
# Creating an instance of the class
obj = MAX()
# Printing the type of the instance
print(type(obj))  # Output: <class '__main__.MAX'>
# Program to create class with data members
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Creating an instance of the class
person1 = Person("Alice", 30)
# Accessing data members
print(f"Name: {person1.name}, Age: {person1.age}")  #

# Program for linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
    
# Program for binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [10, 20, 30, 40, 50]
target = 40
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# program to play sound 
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000   # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

#import playsound
#playsound.playsound('path_to_sound_file.mp3', True) 

# program to play video
import cv2
cap = cv2.VideoCapture('path_to_video_file.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
