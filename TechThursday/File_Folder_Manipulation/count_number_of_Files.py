import os

# Path IN which we have to count files and directories
PATH = "E:\Prasun\Python\TechnicalThursday"   # Give your path here



fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:',root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

print('Number of files',fileCount)
print('Number of Directories',dirCount)
print('Total:',(dirCount + fileCount))


#Modify this Program to ignore the git directories and count only files of type .txt