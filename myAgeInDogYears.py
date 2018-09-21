"""
Time moves quickly for dogs. 8 years in a human's life is like 45 years in a dog's life! How old would you be if you were a dog?

Here's how you convert your age to dog years:
The first two human years of a dog's life count as 10.5 dog years each.
Each human year following counts as 4 dog years.

Write a program to find your age in dog years.
"""

myAge = int(input("Enter your age :"))
twoYrs = 10.5 * 2
laterYrs = (myAge-2) * 4
dogYrs = twoYrs + laterYrs
print("My age in Dog Years :", dogYrs)