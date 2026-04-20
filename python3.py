"""
3.Write a program to read a file named data.txt. If the file does not exist,

handle the error and print "File not found".

"""

try:
    file = open("demofile.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File Not Found")

