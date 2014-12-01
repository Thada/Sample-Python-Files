#!/usr/bin/python
#Thomas Hada, ID 107758936

#This program takes a file with the contents of command "ls -l" on a 
# Linus/UNIX/Mac OS system, prompts for a month and year, then finds all files
# in the directory with the given date with file size > 12000 bytes.

#Open the document that contains the directory's information:
f = open("listing.txt")

#This will read user input to search the file for specific dates:
month = raw_input("Enter a month: ")
year = raw_input("Enter a year: ")

#This loop will go through each line in the .txt file and find entries where
# the month and year match the user's input, and will print the results only
# if the file is greater than 12000 bytes:
for eachline in f:
    a = eachline.split()
    if month == a[6] and year == a[7] and int(a[4]) > 12000:
        print eachline
        
f.close()
