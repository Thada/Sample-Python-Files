#!/usr/bin/python
#Thomas Hada, ID 107758936

#This program creates a list of numbers and then prints a list of prime
# numbers in that list.

#Create the list of numbers between 2 and 1000 and store in a variable:
a = range(2,1001)

#Create a place to store the prime numbers:
primes = []

#A loop that will erase all numbers that are multiples of previous numbers
# and store all prime values:
for value in a:
    primes.append(a[0])
    a = filter(lambda x: x % value != 0, a)
    if a == []:
        break
    if max(primes) == a[0]:
        primes.pop()
        
#Print the list of all prime numbers between 2 and 1000:
print primes



