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

