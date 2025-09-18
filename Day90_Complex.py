# read csv file using pandas, print shape and display
import pandas as pd
file = pd.read_csv("data.csv")
print(file.shape)
print(file.to_string)

import csv

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)   # Convert to list of rows
    
    # Shape of CSV: rows x columns
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    
    print(f"Shape of CSV file: {rows} rows × {cols} columns\n")
    
    # Display as string
    for row in data:
        print(", ".join(row))

# Example
read_csv_file("sample.csv")


import numpy as np
def read_csv_numpy(filename):
    data = np.genfromtxt(filename, delimiter=",", dtype=str)
    
    # Shape of CSV
    print(f"Shape of CSV file: {data.shape[0]} rows × {data.shape[1]} columns\n")
    
    # Display as string
    for row in data:
        print(", ".join(row))

# Example
read_csv_numpy("sample.csv")


from PIL import Image
img = Image.open("image.JPEG")
rotated_img = img.rotate(90)
rotated_img.show()

import cv2

# Load image
image = cv2.imread("your_image.jpg")

# Get image dimensions
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Rotate image by 45 degrees
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

# Show and save result
cv2.imshow("Rotated Image", rotated)
cv2.imwrite("rotated_image.jpg", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
