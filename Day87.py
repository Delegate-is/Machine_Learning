def is_palindrome(input_string):
    input_string = str(input_string)
    result = input_string[::-1]
    return result

input_value = 254
reversed_value = is_palindrome(input_value)
if reversed_value == str(input_value)[::-1]:
    print(True)
else:
    print(False)

def is_palindrome(input_string):
    reversed_string = input_string[::-1]
    return input_string == reversed_string


#Generate string password length given by user
import string
import random

size = int(input("Enter length of password: "))
result = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=size))
print("Strong Psswd is "+str(result))

# Show image to user using open_cv
import cv2
cv2.imread("image.png")
cv2.imshow("Image Title", img)
cv2.waitKey(0)

