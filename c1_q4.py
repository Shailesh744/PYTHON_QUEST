# Write a Python program to print the contents of a directory using the `os` module. Search online for the function that does that
import os
directory_path = "/"
contents = os.listdir(directory_path)
for i in contents:
    print(i)