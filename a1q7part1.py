#!/usr/bin/python
#Thomas Hada, ID 107758936

#This program creates a list of values, eliminates all elements that
# are multiples of the first element, then prints the remaining list.

#Create the list of numbers between 2 and 1000 and store in a variable:
a = range(2,1001)

#Create a place to store the prime numbers:
primes = []

#Filter to erase all elements that are multiples of 2:
a = filter(lambda x: x % a[0] != 0, a)
print a
