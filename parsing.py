#use the provided "3DBenchy.gcode" file
filePath = input("File Path: ")

fileRead = open(filePath, 'r')

fileData = fileRead.readlines()

print(fileData)
