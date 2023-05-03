import os
import shutil

path = r"C:/Users/mati/Desktop/Nowy folder/"
fileName = os.listdir(path)
folderNames = ['csv files', 'image files', 'text files']
for loop in range(0, 3):
    if not os.path.exists(path + folderNames[loop]):
        print(path + folderNames[loop])
        os.makedirs(path + folderNames[loop])

for file in fileName:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    else:
        print("some files in this path are not moved")
