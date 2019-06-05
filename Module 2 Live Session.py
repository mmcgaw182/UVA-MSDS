# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:36:11 2019

Module 2 Live Session Assignment: Python
@authors: Maxwell McGaw, Cory Yemen
IDs: mm9tk, cry4b
"""

# File: pyScript19
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Object-oriented programming (OOP) - Student Class

class Student:
    # fields: name, id, grades(a list)
    
    #Local variable
    #grades = [] # initially empty
    
    def __init__(self, name, id):  # constructor
        self.name = name
        self.id = id
        self.grades = []

    
    def addGrade(self, grade): # add the grade to the list of grades
        self.grades.append(grade)
    
    def showGrades(self): # displaying the grades
        grds = '' # empty string
        for grade in self.grades: # Loop through grades list
            grds += str(grade) + ' '  # assign each grade to the string grds
        return grds
    
    def __str__(self):
        return "Name: " + self.name + " ID: " + str(self.id) + " Grades: " + str(self.grades)
    
    def average(self):                                 
        return 'Average Grade: ' + str(sum(self.grades)/len(self.grades))
    
#==================================================
    
student1 = Student('Jones', '123')
#print(str(student1.name) + ', ' + str(student1.id)) # Output: Jones, 123
student1.addGrade(88)
student1.addGrade(72)
student1.addGrade(100)
#print("Grades: " + student1.showGrades()) # showing grades for student1
# print(student1) # Will NOT work, since we do not have a "to-string" (__str__) method
# Output of the above line will be a memory address like:
#      <__main__.Student object at 0x00000220B8611BE0>
print(student1)
print(student1.average())
#==================================================

# ** TO THINK ABOUT: **
# This is fine, however, what happens if you create a second Student object??
# Local ("global") variable grades (a list - which is a mutable object) will
# accumulate grades from ALL students... this behavior is not what we want. 
# Uncomment lines 46-51 below and see what happens.  How would you fix this?? 
# For now, the above file is fine for the above scenario. 

# =============================================================================
s2 = Student('Clayton', '115')
#print(str(s2.name) + ', ' + str(s2.id)) 
s2.addGrade(85)
s2.addGrade(95)
s2.addGrade(99)
print(s2)
#print("Grades: " + s2.showGrades())
print(s2.average())  # !!!

s3 = Student('Max', '100')
#print(str(s3.name) + ', ' + str(s3.id)) 
s3.addGrade(100)
s3.addGrade(99)
s3.addGrade(98)
print(s3)
#print("Grades: " + s3.showGrades())
print(s3.average()) 
# =============================================================================