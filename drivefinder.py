import os
import shutil

drive_list = set(os.listdir("/Users/amol/Downloads/Socials23"))
original = set(os.listdir("/Users/amol/Downloads/socials_pics"))

difflist = original.difference(drive_list)

origin = "/Users/amol/Downloads/socials_pics/"
target = "/Users/amol/Downloads/missing/"

for filename in difflist:
    shutil.copy(origin + filename, target + filename)
    print(f"{filename} done")

print("success")
