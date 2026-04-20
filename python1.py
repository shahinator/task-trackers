# Problem: Student Result System
# Objective:
# Create a Student class to calculate and display a student's result.
# Requirements:
# ● Class name: Student
# ● Instance variables:
# ○ name
# ○ marks (a list of numbers, e.g. [70, 80, 75])
# Methods:
# 1. get_average()
# 👉 Calculate and return the average of the marks
# 2. get_grade()
# 👉 Return grade based on average:
# ● 80 and above → A
# ● 60–79 → B
# ● 40–59 → C
# ● Below 40 → F
# 3. display_result()
# 👉 Print:
# ● Name
# ● Average
# ● Grade
# Example Output:
# Name: Rahim
# Average: 75
# Grade: B

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 
    
    def get_avarage(self):
        return sum(self.marks)/ len(self.marks)
    def get_grade(self):
        avg = self.get_avarage()
        if avg >= 80:
            return "A"  
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "F"
    def display_result(self):
        print("Name:", self.name)
        print("Average:", self.get_avarage())
        print("Grade: ", self.get_grade())
    
s=Student("Rahim", [70, 80, 75])
s.display_result()