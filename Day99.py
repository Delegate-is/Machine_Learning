# search pattern anything then uppercase letter
import re
user_string = input("Enter a string: ")
x = re.search('.*[0-9]+[_]+[A-Z]+', user_string)
if x:
    print("Matching....")
else:
    print("Not Matching....")

# check whether user password is strong or not
import re
password = input("Enter your password: ")
# ('[a-z]+[A-Z]+[0-9]+[@$!%*?&]+$', password)
x = re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password)
if x:
    print("Strong Password")
else:
    print("Weak Password")

# show text on image
from PIL import Image, ImageDraw

img = Image.open("image.jpeg")
text = "Hello, World!"
draw_img = ImageDraw.Draw(img)
draw_img.text((10, 500), text, (234, 34, 23))
img.show()

# program to join two images
from PIL import Image
img1 = Image.open("image.jpeg")
img2 = Image.open("image.jpeg")
img3 = Image.new('RGB', (img1.width + img2.width, max(img1.height, img2.height)))
img3.paste(img1, (0, 0))
img3.paste(img2, (img1.width, 0))
img3.show()