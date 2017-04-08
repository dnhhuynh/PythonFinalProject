#Import
import random

#Global dictionary of colors
colors = {0 : 'RED', 1 : 'YELLOW', 2 : 'BLUE', 3 : 'GREEN', 4 : 'BLACK', 5 : 'WHITE'}

#Difficult Option
def selectDifficult():
  difficulty = 0
  acceptable = false
  
  #Determines if input is valid
  input = requestString("Please select a difficulty: \nType '1' for Easy \nType '2' for Normal \nType '3' for Hard")
  if input == '1' or input == '2' or input == '3':
    acceptable = true
    
  #While loop to continuously prompt the user to input a valid option
  while acceptable == false:
    input = requestString("Input is not valid! Please select a difficulty: \nType '1' for Easy \nType '2' for Normal \nType '3' for Hard")
    if input == '1' or input == '2' or input == '3':
      acceptable = true
  
  if input == '1':
    difficulty = 4  #EASY sets the number of beads to FOUR
  if input == '2':
    difficulty = 5  #NORMAL sets the number of beads to FIVE
  if input == '3':
    difficulty = 6  #HARD sets the number of beads to SIX
    
  return difficulty
  
#Code Generator
def generateMaster(mainCode, numBeads, colors):

  #For loop to append a random color to our main code list
  for x in range(0, numBeads):
    bead = random.randrange(0, 6, 1)
    mainCode.append(colors[bead])
  
#Main Function
def masterMind():
  #Variables
  mainCode = []                    #List variable to hold master code
  numBeads = selectDifficult()     #Variable to hold number of beads in code
  
  #Function Calls
  generateMaster(mainCode, numBeads, colors)
    
  #Outputs
  print(mainCode)
  
#Static Call of Main
masterMind()
