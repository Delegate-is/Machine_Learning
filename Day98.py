# display image with other library than pil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread("image.jpeg")
imgplot = plt.imshow(img)

# Program where string start with digit not char
import re
user_string = input("Enter a string: ")
x = re.search('[0-9]$', user_string)
if x:
    print("Matching....")
else:
    print("Not Matching....")
    
# program to match 0-5 to ending of string
import re
user_string1 = input("Enter a string: ")
x1 = re.search('[0-5]_+$', user_string1)
if x1:
    print("Matching....")
else:
    print("Not Matching....")
    
# display image with pil library
from PIL import Image
img = Image.open("image.jpeg")
img.show()