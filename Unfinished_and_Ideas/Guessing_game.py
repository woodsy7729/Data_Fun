#Guessing game

import random
computersnumber = random.randint(0,100)
prompt = "Guess a number between 0 and 100 --->"
while True:
	playersguess = input(prompt)
	if computersnumber==int(playersguess):
		print("Correct! Well done!")
		break
	elif computersnumber > int(playersguess):
		print("too low")
	else:
		print("too high")

