# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:09:08 2019

Module 3 Live Session Assignment: Exception Handling

@author: Maxwell McGaw

ID: mm9tk
"""

try:
    name = input("Enter the name of a file: ") #filenotfound
    file = open(name, 'r')
    
    numer = int(input("Enter a numerator: "))
    denom = int(input("Enter a denominator: "))
    quotient = numer / denom
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))


#TypeError
except TypeError:
    print("** Type Error! **")
    
#ValueError
except ValueError:  # for value error
    print("** Value Error! **")
    

#ZeroDivisionError
except ZeroDivisionError:  # for divide by zero error
    print("** Cannot divide by zero! **")
    denom = int(input("Enter a non-zero denominator: "))
    quotient = numer / denom
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))

#ArithmeticError
except ArithmeticError:  # for general arithmetic error
    print("** You caught a general arithmetic error! **")
    denom = int(input("Enter a non-zero denominator: "))
    quotient = numer / denom
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))
    
#FileNotFoundError
except FileNotFoundError:
    print("** FileNotFoundError >> Cannot open file! **")
    name = input("Enter the name of a file to open: ") # w2filegrades.txt
    file = open(name, 'r')    

#IOError
except IOError:  # for general IO errors
    print("** You caught a general IOError! **")
    name = input("Enter the name of a file to open: ") # w2filegrades.txt
    file = open(name, 'r')

#Exception
except Exception:
    print("** You found an error! **")
