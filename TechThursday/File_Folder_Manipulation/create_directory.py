import os

path = "E:\Prasun\Python\TechnicalThursday\TechThursday\File_Folder_Manipulation\Tests"




try:

    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)



filename = "TechThursday\File_Folder_Manipulation\\Tests\\abc.txt"
with open(filename, 'a') as file:
    file.writelines( "I'm Writing this")



# os.remove(filename)

# os.rmdir(path)


