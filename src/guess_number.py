# This is an outline for a game "Guess a number"
# Built with Python to try out the idea
# and to have practice in basics of Python

# global value. Might not need it
generated_number = 0

# player abstract class
class Player:
	def __init__(self, name, id):
		self.name = name
		self.id =  id

# to generate a number to guess and to encrypt it
# param: min, max for selected dificulty or for id generation
from random import randint
def generate_number(min, max):
	return randint(min, max)

# ask player's input
def game_input():
	generated_number = generate_number(0, 10)
	guess = ''
	# while not(guess.isdigit()):
	# 	guess = input("Please enter a number from 0 to 10: ")
	# if int(guess) == generated_number:
	# 	print("Wow! You guess correctly! Congratulations!")
	# else:
	# 	print("Sorry, your guess is incorrect")
	while True:
		try:
			guess = int(input("Please enter a number from 0 to 10: "))
		except:
			print("That doesn't seem like a number")
			continue
		else:
			if int(guess) == generated_number:
				print("Wow! You guess correctly! Congratulations!")
				break
			else:
				print("Sorry, your guess is incorrect")
				break


# game dificulty:
# num 0 to 10 -2 tries
# num 0 to 20 -3 tries
# num 0 to 100 - 10 tries
# num 0 to 500 - 15 tries
def select_dificulty():
	pass

# start game
# take user input
# compare to generated number
# give result
# count tries
print('Welcome to "Guess a number" game')
id = generate_number(1000, 10001)
name = ""

while len(name.strip('.#!? ')) < 1:
	name = input("Enter your name: ")

player = Player(name, id)

while True:
	play = input(f" Hey {name}! Want to play 'Guess a number?' \n Please, enter 'Yes' or 'No'")
	if play == "No":
		print(f"See you next time {name}!")
		break
	elif play == "Yes":
		game_input()
	else: print("Let's try again. \n Please, enter 'Yes' or 'No'")


