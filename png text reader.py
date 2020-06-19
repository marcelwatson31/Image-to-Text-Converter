import pytesseract as tess
# Makes pytesseract in the environment PATH so that you can run the excutable
tess.pytesseract.tesseract_cmd = r'C:\Users\marce\AppData\Local\Tesseract-OCR\tesseract.exe'
# PIL allows the image file type to be opened 
from PIL import Image


#First Instance is without it being a reusable function where you only have to enter in the image file path
'''img = Image.open('C:/Users/marce/Desktop/booktext.png')
text = tess.image_to_string(img)
print(text)'''

#Made it into a function for reuse.


def Image_text_converter(img):
    img = Image.open(img)
    text = tess.image_to_string(img)
    print(text)
#Your directory path will be diffrent 

Image_text_converter('C:/Users/marce/Desktop/booktext.png')

print('\n \n')


Image_text_converter('C:/Users/marce/Desktop/WhiteFangBook.jpg')