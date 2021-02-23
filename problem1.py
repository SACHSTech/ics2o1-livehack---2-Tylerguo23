"""
----------------------------------------------------------------------
Name:      problem1.py

Purpose:   This program will determine the type of martian being detected using the number of eyes and antenna being inputted
 
Author:    Guo.T
 
Created:   23/02/2021
----------------------------------------------------------------------
"""
print("******* Martian Classifier ********")
print()

#take user input for the number of eyes and antennas
antennas = int(input("How many antennas are detected?: "))
eyes = int(input("How many eyes are detected?: "))

#boolean to track whether at least one of the conditions are met
found_alien = False

#check each condition and output 
if antennas >= 3 and eyes <= 4:
  print("Life form detected: AudreyMartian")
  found_alien = True
if antennas <= 6 and eyes >= 2:
  print("Life form detected: MaxMartian")
  found_alien = True
if antennas <= 2 and eyes <= 3:
  print("Life form detected: BrooklynMartian")
  found_alien = True
if antennas == 0 and eyes == 2:
  print("Life form detected: MattDamonMartian")
  found_alien = True

#if none of the above conditions are met, output "No life form detected"
if not found_alien:
  print("No life form detected")