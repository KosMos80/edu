#!/usr/bin/python2.7

import time
import math
import random

'''
Game Guess the number.
The computer generates a number between 0 and 999 (using random number generation) 
and the user guesses it. 
At each step, the guesser makes a guess, and the one who came up with the number 
reports how many digits from the number were guessed and how many of the guessed 
digits occupy the correct places in the number. For example, if the number 725 is 
guessed and the assumption is made that the number 523 is guessed, then two numbers 
are guessed (5 and 2), and one of them takes the correct position.
'''

def CountEqual(first, second):
	count = 0
	if(first%10 == second%10):
		count += 1
	if(first/10%10 == second/10%10):
		count += 1
	if(first/100 == second/100):
		count += 1
	return count

def CountSostav(first, second):
	count = 0
	first_arr = [first/100, first/10%10, first%10]
	second_arr = [second/100, second/10%10, second%10]
	for fr in first_arr:
		for sc in second_arr:
			if(fr == sc):
				if(fr != 0):
					count += 1
	return count

def RandomFirst(first, pos):
	ex = 1
	while ex:
		rnd = random.randint(1,9)
		if(CountSostav(first, rnd) == 0):
			ex = 0
	for i in range(pos):
		rnd *= 10
	first = first + rnd
	return first

def SetFirst():
	first = 0
	first = RandomFirst(first, 0)
	first = RandomFirst(first, 1)
	first = RandomFirst(first, 2)
	return first
	
def ReadChislo():
	ex = 1
	while ex:
		second = int(input("Vvedi chislo: "))
		second_arr = [second/100, second/10%10, second%10]
		if((second_arr[0] != second_arr[1]) and (second_arr[0] != second_arr[2]) and (second_arr[1] != second_arr[2])):
			ex = 0
		else:
			print "Incorrect numder. Chisla ne doljni bit odinakovimi i imet nuli"
	return second

if(__name__ == "__main__"):
	first = SetFirst()
	print
	print " Computer pridumal chislo ... "

	ex = 1
	while ex:
		second = ReadChislo()
		count_s = CountSostav(first, second)
		print "Sovpadeniya: ", count_s
		count_e = CountEqual(first, second)
		print "Na svoih mestah: ", count_e
		if(count_e == 3):
			ex = 0
		else:
			print " try again .... "

	print "OK. It's correct number ..."
