import random

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
  
def masterMind():

  mainCode = []
  color = {0 : 'RED', 1 : 'YELLOW', 2 : 'BLUE', 3 : 'GREEN', 4 : 'BLACK', 5 : 'WHITE'}
  numBeads = selectDifficult()
  
  for x in range(0, numBeads):
    bead = random.randrange(0, 6, 1)
    mainCode.append(color[bead])
    
  print(mainCode)
  
masterMind()
