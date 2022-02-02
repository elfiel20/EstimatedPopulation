#This is Exercise 5's Code
#This code has the goal of producing an estimaton for the population
#given an amount of years from now

#Asking for the amount of years from the user


import math


print("This is a program to calculate the estimated population for a given amount of years in the furute ")
y=float(input("Insert an amount of years from the present "))

#First the code is converting years to seconds
#This is done in steps years, then days, then hrs, then mins, and finally secs

#d=the amount of days

d=y*365

h=d*24

m=h*60

s=m*60

#Now S (in seconds) is going to be used instead of Y
#for all subsequent operations


P=328000000+((s/8)-(s/12)+(s/33))

print("Future Population is approximately equal to:")

#P is for the future Population

print(P)






