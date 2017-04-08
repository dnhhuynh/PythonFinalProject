import random

#Global Variables
colors = {0 : 'RED', 1 : 'YELLOW', 2 : 'BLUE', 3 : 'GREEN', 4 : 'BLACK', 5 : 'WHITE'}

#Difficult Option
def selectDifficult():
  difficulty = 0
  
  input = requestString("Please select a difficulty: \nType '1' for Easy \nType '2' for Normal \nType '3' for Hard")
  
  if input == '1':
    difficulty = 4
  if input == '2':
    difficulty = 5
  if input == '3':
    difficulty = 6
    
  return difficulty
  
#Code Generator
def generateMaster(mainCode, numBeads, colors):
  for x in range(0, numBeads):
    bead = random.randrange(0, 6, 1)
    mainCode.append(colors[bead])
  
#Main Function
def masterMind():

  mainCode = []
  numBeads = selectDifficult()
  
  generateMaster(mainCode, numBeads, colors)
    
  print(mainCode)
  
#Static Call of Main
masterMind()
