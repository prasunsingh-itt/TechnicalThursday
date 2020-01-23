#Script to count number of Words

def countWords(fileName):
    numwords = 0
    numchars = 0
    numlines = 0

    with open(fileName, 'r') as file:
        for line in file:
            wordlist = line.split()
            numlines += 1
            numwords += len(wordlist)
            numchars += len(line)

    print ("Words: ", numwords)
    print ("Lines: ", numlines)
    print ("Characters: ", numchars)


countWords('E:\Prasun\Python\TechnicalThursday\TechThursday\File_Folder_Manipulation\count_number_of_Files.py')

