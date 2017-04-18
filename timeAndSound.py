# Time and Sound Functionality for MasterMind:  

import time

start_time = time.time()

#Global sound files: 
win = makeSound('/path/to/Win.wav')
lose = makeSound('/path/to/Lose.wav')
correct = makeSound('/path/to/correctAnswer.wav')
highScore = makeSound('/path/to/highScore.wav')

# Call these sounds files via sound(win), sound(lose), sound(correct), and sound(highScore), where ever they are needed throughout the program. 

# main() and other functions()

def someExitFunction(): 
	
	elapsed_time = time.time() - start_time
	print 'It took you ", elapsed_time, "to complete MasterMind!'

def sound(s): 
	play(s)
