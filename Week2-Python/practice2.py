number = 78
user_guess= input("Guess a number ")
number_guesses= 0
guesses_left= 5


while number_guesses<5:
	while int(user_guess) != number:
		if int(user_guess) > number:
			print("Your guess is too high!")
			number_guesses+=1
			guesses_left-= number_guesses
			user_guess= input("Try again :( You have " + int(guesses_left) + " guesses left.")
		else:
		 	print("Your guess is too low!")
		 	number_guesses+=1
		 	guesses_left)-= number_guesses
		 	user_guess= input("Try again :( You have " + int(guesses_left) + " guesses left.")
		 
if int(user_guess)== number:
	print("You guessed right!!! :) ")
	print("Game Over")