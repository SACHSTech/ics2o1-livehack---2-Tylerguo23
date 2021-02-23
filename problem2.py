"""
----------------------------------------------------------------------
Name:      problem2.py

Purpose:   This program will determine if the three side lengths inputted by the user can form a triangle
 
Author:    Guo.T
 
Created:   23/02/2021
----------------------------------------------------------------------
"""
print("******* Traingle Checker ********")
print()

#take the three side lengths as input
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

#check if condition is met and output
if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
  print("The figure is a traingle")
else:
  print("The figure is NOT a traingle")