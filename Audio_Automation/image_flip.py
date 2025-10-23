# Counting number of pixel on image


#Image fliping in python using PIL library
from PIL import Image
# Open an image file
with Image.open("image.jpeg") as img:
    # Flip the image horizontally
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    # Save the flipped image to a new file
    flipped_img.save("flipped_image.jpg")
    print("Flipped image saved as flipped_image.jpg")
    
# Extracting text from image using pytesseract
try:
    import pytesseract
except Exception as e:
    import sys
    print("pytesseract is not installed or could not be imported:", e, file=sys.stderr)
    print("Install with: pip install pytesseract and make sure the Tesseract OCR engine is installed and on PATH.", file=sys.stderr)
    pytesseract = None

from PIL import Image
# Open an image file
if pytesseract is not None:
    with Image.open("image_with_text.jpeg") as img:
        # Use pytesseract to do OCR on the image
        try:
            text = pytesseract.image_to_string(img)
        except Exception as e:
            import sys
            print("Failed to run pytesseract:", e, file=sys.stderr)
            text = ""
        # Print the extracted text
        print("Extracted Text:")
        print(text)
else:
    import sys
    print("Skipping OCR because pytesseract is not available.", file=sys.stderr)
# Note: Make sure to have Tesseract OCR installed on your system for pytesseract to work.
