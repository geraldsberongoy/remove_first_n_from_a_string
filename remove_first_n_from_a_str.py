# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# pseudocode
# 1. print "Removing characters from a string"
# 2. def function(pynative, number)
# 3.    print orig string
# 4.    print removed string

# Code
def remove(orig, num):
    print(f"The original word is {orig}.")
    print(orig[num::])

remove("pynative", 2)
remove("pynative", 4)