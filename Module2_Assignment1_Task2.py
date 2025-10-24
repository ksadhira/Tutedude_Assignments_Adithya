'''Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''
First_Name = input("Enter your first name: ")
Last_Name = input("Enter your last name: ")
Full_Name = First_Name + "_" + Last_Name
print("Hello ",Full_Name + ",\nWelcome! \nHope you are doing great today.")