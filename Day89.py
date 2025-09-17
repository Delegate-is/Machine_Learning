# Program to find resolution of image
import cv2
img = cv2.imread("image.png")
h = img.shape[0]
w = img.shape[1]
print(h)
print(w)
print(str(h)+ " x " + str(w))

import os
# Change this to your image path
file_path = "your_image.jpg"
# Get size in bytes
file_size = os.path.getsize(file_path)
# Convert to MB
size_in_mb = file_size / (1024 * 1024)
print(f"Image size: {size_in_mb:.2f} MB")

# Program to blur an image
import cv2
img = cv2.imread("image.png")
blur_Image = cv2.blur(img,(10,10))
cv2.imshow("Title of real image", img)
cv2.imshow("Title image", blur_Image)
cv2.waitKey(0)