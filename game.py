#this is the "game.py" file...

import random

print("Welcome 'Player One' to My Rock, Paper, Scissors Game")


#Processing user inputs
user_input = input("Please choose one 'Rock', 'Paper', 'Scissors'")
user_input = user_input.lower()


#Validating user inputs
valid_options = ["rock", "paper", "scissors"]
if user_input in valid_options:
	print("You choose:", user_input)


	#Simulating computer selection
	computers_choice = random.choice(valid_options)
	print("Computer chooses:", computers_choice)


	#Determining winner
	if user_input == computers_choice:
		print("TIE")	
	elif user_input == "rock":
		if computers_choice == "scissors":
			print("You Win!")
		else:
			print("You Lost.")
	elif user_input == "paper":
		if computers_choice == "rock":
			print("You Win!")
		else:
			print("You Lost.")
	elif user_input == "scissors":
		if computers_choice == "paper":
			print("You Win!")
		else:
			print("You Lost.")	

	print("Thanks for Playing!")							


if user_input not in valid_options:
	print("INVALID CHOICE. TRY AGAIN")			
	exit()