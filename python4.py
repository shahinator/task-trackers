"""
Write a program that takes user input and appends it to a file named

notes.txt without deleting existing content.

"""
text = input("Enter your note: ")
with open("notes.txt", "a") as file:
    file.write(text)
