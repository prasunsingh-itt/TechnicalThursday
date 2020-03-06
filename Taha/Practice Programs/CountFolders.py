import os
path = input("Enter the path with escasping blackslashes : \n")
dir_count = 0
file_count = 0
for _, dirs, files in os.walk(path):
        dir_count += len(dirs)
        file_count += len(files)
print (dir_count)
print (file_count)




# C:\\Users\\taha.masavi\\Desktop\\Technical Thursday\\TechnicalThursday