# Put your code here
import random # import the random module

player_name = raw_input("Hi! What's your name?\n")
print "{}, I'm thinking of a number between 1 and 100.".format(player_name)
print "Try to guess my number!"

random_number_generated = randon.randint(1, 100)
def guessing_game():
	guess = int(raw_input("Your guess? "))
	count = 0
	if guess != random_number_generated:
		count += 1
		if guess > random_number_generated:
			print "Your guess is too high! Try again!"
		else:
			print "Your guess is too low! Try again!"
	else:
		print "Congratulations, {}! You found the number in {} tries!".format(player_name, count)

guessing_game()
