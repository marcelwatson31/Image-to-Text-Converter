# Image-to-Text-Converter
Python Tesseract app that allows you to convert image text to text.


Note : This assumes that you already have python downloaded on your computer.
Note : VS Code was used for this application

The first step needed to allow for this program to work with your image files you would like is to (Windows Users) pip install pytesseract in your command terminal. 

After it will download the library needed.

Next you will need to navigate to https://github.com/UB-Mannheim/tesseract/wiki  and download the tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe  or 32 bit version. Run the setup and configure to your liking however you can next until finished.


You will want to then find the location of the full tesseract.exe directory PATH and copy and paste it in the 3rd line of Code inbetween the quotes r''.

Then place the location paths of the images you would like to use in the function call if you don't want to use my pictures and run the program.

You should see the text that appears in the image which works pretty well but has trouble with letters or characters not standardly written.


The use of this application and library pytesseract are numerous would suggest to learn more about Tesseract.
