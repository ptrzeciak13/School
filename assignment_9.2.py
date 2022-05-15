# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Patrick Trzeciak
# Creation Date: 05/10/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

# The random import is not needed as you are not using the random function
#import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    # Here I have moved the print line to the top of the function.
    # The cave variable is an input after the print line
    # The while statement should be an if statement and all be equal to one number and not both as your function will return the same thing if the user enters 1 or 2
    # The return function should state what you want it to return, in this case you do not want to return the variable that is already defined.
    #cave = ''
	#while cave != '1' and cave != '2':
		
		#print('Which cave will you go into? (1 or 2)')
		#cave = input()

	#return caves
	print('Which cave will you go into? (1 or 2)')
	cave = input()
	if cave == '1':
		return 'friendlyCave'

# Here you have a spelling error, chosen should equal choose.
def checkCave(chooseCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	#commented out this line as it is not needed for this code. You do not want to randomize the number or the out come may not be what the user choose.
	#friendlyCave = random.randint(1, 2)

	# String is not needed here as you are returning a statement in chooseCave function.
	# Spelling error chosenCave should be chooseCave
	if chooseCave == 'friendlyCave':
		print('Gives you his treasure!')
	else:
		# Here you are missing the parentheses around what you are printing.
		print('Gobbles you down in one bite!')

playAgain = 'yes'
# In this while statement you need the double equals sign
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	# Spelling error chosenCave should be chooseCave
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")

