#!/usr/bin/python
#Thomas Hada, ID 107758936

#This program takes a string input consisting of all 3-digit course numbers
# for 100, 200, and 300 level classes, and outputs the number of courses 
# per category.

#Initialize variables to store the number of each course level:
oneCount = 0
twoCount = 0
threeCount = 0


#Create a variable to collect user input, then split() to separate values:
courses = raw_input("Enter 3-digit course numbers, separated by spaces: ")
a = courses.split()

#Sort the values to prepare calculations:
a.sort()

#A loop that will compare each value to see if they are equivalent.  Duplicate
# values are deleted:
for value in a[1:]:
    if value == a[0]:
        a.pop(a.index(value))

#A loop that will classify and count the number of 100, 200, and 300 courses:
for value in a:
    if value[0] == '1':
        oneCount += 1
    elif value[0] == '2':
        twoCount += 1
    elif value[0] == '3':
        threeCount += 1


#Prints out the number of unique courses, classified by level:
print "100: ", oneCount, "\t200: ", twoCount, "\t300: ", threeCount
