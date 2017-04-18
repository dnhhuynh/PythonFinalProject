#Import
import random

#Global dictionary of colors
colors = ['R', 'G', 'B', 'W', 'Y', 'P']

#Takes two parameters: secret code and guess code and returns a string containing the score
def scoreTurn(cLst, gLst):
    unusedLst = []
    scoreLst = []
    ln = len(cLst)

    for i in range(0, ln):
        unusedLst.append(gLst[i])
        scoreLst.append(cLst[i])
    
    for b1 in range(0, ln):
        if scoreLst[b1] == unusedLst[b1]:
            scoreLst[b1] = 'b'
            unusedLst[b1] = ''
            
    for w1 in range(0, ln):        
        for w2 in range(0, ln):
            if scoreLst[w1] == unusedLst[w2]:
                scoreLst[w1] = 'w'
                unusedLst[w2] = ''

    for i in range(0, 6):
        while colors[i] in scoreLst: scoreLst.remove(colors[i])   
        
    scoreLst.sort()    
       
    scoreStr = ''.join(map(str, scoreLst))
    return scoreStr

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



def chose_color():

  wrong=[]


#level of difficulty 1
  while (len(wrong) != 4):
    userGuess = requestString("Guess a color: ")
    if userGuess not in colors:
      wrong.append(userGuess)
      showInformation("The color you guesses is incorrect, you have used " + str(len(wrong)) + " out of 4 guesses.")
    else:
      showInformation("You have guessed the color") 
    
    for userGuess in colors:
      if (userGuess==len(colors)):
        showInformation("Congratulations you guessed the colors")

#level of difficulty 2
  while (len(wrong) != 5):
    userGuess = requestString("Guess a color: ")
    if userGuess not in colors:
      wrong.append(userGuess)
      showInformation("The color you guesses is incorrect, you have used " + str(len(wrong)) + " out of 5 guesses.")
    else:
      showInformation("You have guessed the color") 
    
    for userGuess in colors:
      if (userGuess==len(colors)):
        showInformation("Congratulations you guessed the colors")

#level of difficulty 3
  while (len(wrong) != 6):
    userGuess = requestString("Guess a color: ")
    if userGuess not in colors:
      wrong.append(userGuess)
      showInformation("The color you guesses is incorrect, you have used " + str(len(wrong)) + " out of 6 guesses.")
    else:
      showInformation("You have guessed the color") 
    
    for userGuess in colors:
      if (userGuess==len(colors)):
        showInformation("Congratulations you guessed the colors")
        
chose_color()
