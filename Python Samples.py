#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:03:48 2021

@author: bennetthall
"""

#These are some of the Python problems that I created in my Python class. 
#The samples below including defining functions, for and while loops, a 
#project that requires user input, and a sample of OOP. 

def my_function(w, x, y, z):
    return w + x - y * z // 4

print(my_function(w = 453, x = 231, y = 512, z = 43))

for x in range (2, 100, 10):
    print(x)
    
def diff21(n):
  if n <= 21:
    return n - 21
  else:
    return (n - 21) * 2

diff21(n = 21)
print(diff21(n = 21))

i = 1
while i < 6:
  print(i)
  i += 1

print(i)

class Cars:
	def __init__(self, make, model):
		self.make = make
		self.model = model

	def love(self):
		print('I love my ' + self.make + self.model)

car1 = Cars('Acura', 'TLX')

print(car1.make)
print(car1.model)
car1.love()

import datetime
firstnamelastname = input('Please enter your first name followed by your last name: ')
names = firstnamelastname.split()
first = names[0].capitalize()
last = names[1].capitalize()
yearborn = int(input('Please enter the year that you were born: '))
monthborn = int(input('Please enter the month you were born: '))
dayborn = int(input('Please enter the day you were born: '))
born = datetime.datetime(yearborn, monthborn, dayborn)
today = datetime.datetime.now()
#print ('You were born: ', born.year, born.month, born.day)
#print ('Today is: ', today.year, today.month, today.day)
difference = today - born
#print(difference)
print ('Dear', first, last, 'you have been in the world', difference.days, 'days.')

