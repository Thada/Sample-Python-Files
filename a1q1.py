#!/usr/bin/python
#Thomas Hada, ID 107758936

#This program reads a set of numbers from the user with one number per line,
# then prints the second largest number in the set.  Type "-99" to exit.

#initialize variables, and prepare for input:
values = []
count = 0
num = input("Enter a set of values, separated by new lines.  Enter -99 to exit; ")

#Appends each value entered to 'values', then sorts in ascending order:
while num != -99:
    values.append(num)
    count = count + 1
    num = input("\nNext value: ")
values.sort()

#Prints to screen the result of the input, finding the second largest value;
if values == []:
    print "No values entered."
elif len(values) == 1:
    print "Only one value entered: ", values[0]
else:
    print "The second largest value is: ", values[(count - 2)]
