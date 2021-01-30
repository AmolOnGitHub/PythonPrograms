import os
import shutil

def getNum(name):
    return name.split("_")[1]

supwPath = "/Users/amol/Desktop/supw photos"
paperPath = "/Users/amol/Desktop/supw photos/Paper"
cookingPath = "/Users/amol/Desktop/supw photos/Cooking"

os.mkdir(paperPath)
os.mkdir(cookingPath)

supwFolder = os.listdir(supwPath)

for picture in supwFolder:
    picturePath = supwPath + "/" + picture
    if "Paper_" in picture:
        newPath = paperPath + "/" + picture
        shutil.move(picturePath, newPath)
    elif "Cooking_" in picture:
        newPath = cookingPath + "/" + picture
        shutil.move(picturePath, newPath)      

paperFolder = os.listdir(paperPath)
cookingFolder = os.listdir(cookingPath)

paperFolder.sort(key = getNum)
cookingFolder.sort(key = getNum)

counter = 1
for picture in paperFolder:
    newName = "Paper_" + str(counter) + ".jpg"
    os.rename(paperPath + "/" + picture, paperPath + "/" + newName)
    counter += 1

counter = 1
for picture in cookingFolder:
    newName = "Cooking_" + str(counter) + ".jpg"
    os.rename(cookingPath + "/" + picture, cookingPath + "/" + newName)
    counter += 1


