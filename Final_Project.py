#Import
import random

#Global dictionary of colors
colors = ['R', 'G', 'B', 'W', 'Y', 'P']
grey = makeColor(192,192,192)
purple = makeColor(255, 0, 255)

#Displays the user's guesses
def fillPeg(screen, round, guess):
  row = 90 + (round - 1) * 60
  for x in range(0, len(guess)):
    if guess[x] == 'R':
      color = red
    if guess[x] == 'G':
      color = green
    if guess[x] == 'B':
      color = blue
    if guess[x] == 'W':
      color = white
    if guess[x] == 'Y':
      color = yellow
    if guess[x] == 'P':
      color = purple
    addOvalFilled(screen, 25 + x * 60, row, 40, 40, color)
    
#Displays the indicator pegs
def fillSmallPeg(screen, round, scoreString, difficulty):
  if difficulty == 4:
    initial = 275
  if difficulty == 5:
    initial = 345
  if difficulty == 6:
    initial = 405
  row = 105 + (round - 1) * 60
  for x in range(0, len(scoreString)):
    if scoreString[x] == 'g':
      color = grey
    if scoreString[x] == 'w':
      color = white
    addOvalFilled(screen, initial + x * 30, row, 15, 15, color)

#Generates a game board with 4 pegs
def easyLayout():
  screen=makeEmptyPicture(400,800,grey)
  for x in range(0,4):
   for y in range(0,10):
     addOvalFilled(screen, 20+x*60, 85+y*60, 50, 50, black)
     addOvalFilled(screen, 270+x*30,100+y*60, 25, 25, black)
  addLine(screen, 265, 80, 265, 680)
  addLine(screen, 0, 80, 600, 80)
  addLine(screen, 0,680, 600,680)
  
  return screen

#Generates a game board with 5 pegs  
def mediumLayout():
  screen=makeEmptyPicture(500,800,grey)  
  for x in range(0,5):
   for y in range(0,10):
     addOvalFilled(screen, 20+x*60,85+y*60, 50, 50, black)
     addOvalFilled(screen, 340+x*30,100+y*60, 25, 25, black)
  addLine(screen, 325, 80, 325, 680)
  addLine(screen, 0, 80, 600, 80)
  addLine(screen, 0,680, 600,680)
  
  return screen
  
#Generates a game board with 6 pegs
def hardLayout(): 
  screen=makeEmptyPicture(600,800,grey)
  for x in range(0,6):
   for y in range(0,10):
     addOvalFilled(screen, 20+x*60,85+y*60, 50, 50, black)
     addOvalFilled(screen, 400+x*30,100+y*60, 25, 25, black)
  addLine(screen, 385, 80, 385, 680)
  addLine(screen, 0, 80, 600, 80)
  addLine(screen, 0,680, 600,680)
  
  return screen
  
#Displays the master code at the bottom of the game mode
def solution(screen,masterCode):
  for x in range(0,len(masterCode)):
   for y in range(0,1):
     addOvalFilled(screen, 20+x*60,685+y*60, 50, 50, black)
     if masterCode[x] == 'R':
       addOvalFilled(screen, 25+x*60,690+y*60, 40, 40, red)
     if masterCode[x] == 'G':
       addOvalFilled(screen, 25+x*60,690+y*60, 40, 40, green)
     if masterCode[x] == 'B':
       addOvalFilled(screen, 25+x*60,690+y*60, 40, 40, blue)
     if masterCode[x] == 'W':
       addOvalFilled(screen, 25+x*60,690+y*60, 40, 40, white)
     if masterCode[x] == 'Y':
       addOvalFilled(screen, 25+x*60,690+y*60, 40, 40, yellow)
     if masterCode[x] == 'P':
       addOvalFilled(screen, 25+x*60,690+y*60, 40, 40, purple)

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
            scoreLst[b1] = 'g'
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
    
#Determines which board to create based on difficulty
def createBoard(difficulty):
  if difficulty == 4:
    screen = easyLayout()
  elif difficulty == 5:
    screen = mediumLayout()
  else:
    screen = hardLayout()
  
  return screen
  
#Main Function
def masterMind():
  #Variables
  mainCode = []                    #List variable to hold master code
  rspdCode = ''                    #List variable to hold user response
  numBeads = selectDifficult()     #Variable to hold number of beads in code
  round = 1
  endGame = false
  
  #Function Calls
  generateMaster(mainCode, numBeads, colors)
  screen = createBoard(numBeads)
  show(screen)

  
 while endGame == false and round <10 :
   round = round+1
   print('This is your %d guess out of 10'%round)
   rspdCode = requestString("Guess colors").strip()
   rspdCode.upper()
  
   if round ==10:
     showInformation ("Sorry you lost :( ")
     endGame == true
   
   if rspdCode in mainCode and rspdCode in colors:
     continue
   else:
     showInformation("Pleace enter 4 colors: 'R' for red, 'G' for green, 'B' for blue, 'W' for white, 'Y' for yellow, and 'P' for purple")
   
   for i in range(0,1):
     print "[%s]" %rspdCode 
     
   if rspdCode == mainCode:
     showInformation(" CongratulationsYou won!!")
       
masterMind()
