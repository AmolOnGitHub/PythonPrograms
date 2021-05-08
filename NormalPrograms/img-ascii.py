import os
from PIL import Image, ImageOps

def char(value):
    value = round(1 - value, 1)
    if value == 0.0:
        return " "
    if value == 0.1:
        return "."
    if value == 0.2:
        return ":"
    if value == 0.3:
        return "-"
    if value == 0.4:
        return "="
    if value == 0.5:
        return "+"
    if value == 0.6:
        return "*"
    if value == 0.7:
        return "#"
    if value == 0.8:
        return "%"
    if value == 0.9 or value == 1:
        return "@"
    

imageName = input("Enter the name of the image you would like to convert: ")
if "/img-ascii" in os.getcwd():
    imagePath = os.getcwd() + "/" + imageName
else:
    imagePath = os.getcwd() + "/img-ascii/" + imageName

image = Image.open(imagePath)

textName = input("Enter the name of the file where you would like to store the art: ")
if "/img-ascii" in os.getcwd():
    textPath = os.getcwd() + "/" + textName
else:
    textPath = os.getcwd() + "/img-ascii/" + textName


print("This image's dimensions are: " + str(image.size))
pixelConst = int(input("Choose the size (in px) that one character will represent: "))
newWidth = round(image.size[0] / pixelConst)
newHeight = round(image.size[1] / pixelConst)

#Resizes Image
print("\nImage resizing....")
image = image.resize((newWidth, newHeight))
print("Resizing finished.")

#Converts image to grayscale
print("\nConverting to grayscale....")
image = ImageOps.grayscale(image)
print("Conversion finished.")
image.show()
#Gets the grayscale value for each pixel
pixelValues = list(image.getdata())
counter = 0
for i in pixelValues:
    pixelValues[counter] = round(i / 255, 1)
    counter += 1

#Starts printing
textFile = open(textPath, "w")
counter = 0
for no in pixelValues:
    textFile.write(char(no))
    counter += 1

    if counter == image.size[0]:
        textFile.write("\n")
        counter = 0