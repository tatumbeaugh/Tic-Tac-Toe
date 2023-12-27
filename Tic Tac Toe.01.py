
# variables:
# number of turns
turns = 1
# status of winner
winner = 0

# variables that represent spots on the board
# row 1 collumn 1
b1 = 0 
# row 1 collumn 2
b2 = 0
# row 1 collumn 3
b3 = 0
# row 2 collumn 1
b4 = 0
# row 2 collumn 2
b5 = 0
# row 2 collumn 3
b6 = 0
# row 3 collumn 1
b7 = 0
# row 3 collumn 2
b8 = 0
# row 3 collumn 3
b9 = 0

# initial instructions
print('Please insert your moves as a coordinate. (ex: 2 1)\n 2 being the collumn and 1 being the row.\n Reference the grid below.')
print (' ','1','2','3')
print ('1', b1, b2, b3)
print ('2', b4, b5, b6)
print ('3', b7, b8, b9)

# checks if anyone has won yet, runs after every turn
def check():
  global winner
  winner = 0

  # tells program that it is a draw
  if turns > 9:
    winner +=3
    
  # X win r1
    #  x x x
    #  - - -
    #  - - -  
  
  if b1 == 'X':
    if b2 == 'X':
      if b3 == 'X':
        winner += 1

  # Y win r1
    #  x x x
    #  - - -
    #  - - - 
  
  if b1 == 'Y':
    if b2 == 'Y': 
      if b3 == 'Y':
        winner += 2
        
  # X win r2
    #  - - -
    #  x x x
    #  - - -  
  
  if b4 == 'X':
    if b5 == 'X':
      if b6 == 'X':
        winner += 1

  # Y win r2
    #  - - -
    #  y y y
    #  - - - 
  
  if b4 == 'Y':
    if b5 == 'Y': 
      if b6 == 'Y':
        winner += 2
        
  # X win r3
    #  - - -
    #  - - -
    #  x x x
  
  if b7 == 'X':
    if b8 == 'X':
      if b9 == 'X':
        winner += 1
  
  # Y win r3
    # - - -
    # - - - 
    # y y y
   
  if b7 == 'Y':
    if b8 == 'Y': 
      if b9 == 'Y':
        winner += 2

  # X win c1
    # x - -
    # x - -
    # x - -  
    
  if b1 == 'X':
    if b4 == 'X':
      if b7 == 'X':
        winner += 1
  
    # Y win c1
      # y - - 
      # y - -
      # y - - 
    
  if b1 == 'Y':
    if b4 == 'Y': 
      if b7 == 'Y':
        winner += 2
          
    # X win c2
      # - x -
      #  - x -
      #  - x -  
    
  if b2 == 'X':
    if b5 == 'X':
      if b8 == 'X':
       winner += 1
  
    # Y win c2
      # - y -
      #  - y -
      #  - y - 
    
  if b2 == 'Y':
    if b5 == 'Y': 
      if b8 == 'Y':
        winner += 2
          
  # X win c3
    # - - x
    # - - x
    # - - x
  
  if b3 == 'X':
    if b6 == 'X':
      if b9 == 'X':
        winner += 1
    
    # Y win c3
      # - - y
      # - - y 
      # - - y
    
  if b3 == 'Y':
    if b6 == 'Y': 
      if b9 == 'Y':
        winner += 2
          
    # X win d1
      # x - -
      # - x -
      # - - x  
    
  if b1 == 'X':
    if b5 == 'X':
      if b9 == 'X':
       winner += 1
  
    # Y win d1
      #  y - -
      #  - y -
      #  - - y 
    
  if b1 == 'Y':
    if b5 == 'Y': 
      if b9 == 'Y':
        winner += 2
          
    # X win d2
      # - - x
      # - x -
      # x - -
    
  if b3 == 'X':
    if b5 == 'X':
      if b7 == 'X':
        winner += 1
    
    # Y win d2
      # - - y
      # - y - 
      # y - -
    
    if b3 == 'Y':
      if b5 == 'Y': 
        if b7 == 'Y':
         winner += 2

# displays board, called after every turn
def display():  
  print (b1, b2, b3)
  print (b4, b5, b6)
  print (b7, b8, b9)

# input is in this while loop, ends when winner is declared
while winner == 0:

  # determines player
  if turns % 2 == 0:
    player = 'Y'
  else:
    player = 'X'

  # takes in input and splits into two variables
  y = input("Player " + player + 's turn: ' )
  collumn,row = y.split()
  row = int(row)
  collumn = int(collumn)


  # changes board based on user input
  # row 1
  if row == 1:
    # 1 1
    if collumn == 1:
      b1 = player
    # 1 2
    elif collumn == 2:
      b2 = player
    # 1 3
    elif collumn == 3:
      b3 = player
  
  # row 2
  if row == 2:
    # 2 1
    if collumn == 1:
      b4 = player
    # 2 2
    elif collumn == 2:
      b5 = player
    # 2 3
    elif collumn == 3:
      b6 = player
  
  # row 3
  if row == 3:
    if collumn == 1:
      b7 = player
    # 3 2
    elif collumn == 2:
      b8 = player
    # 3 3
    elif row == 3 and collumn == 3:
      b9 = player

  # adds to variable that determines player
  turns += 1

  # runs functions to check for winner and display board
  display()
  check()

# prints winner or draw
if winner == 3:
  print('Draw!')
elif winner == 1:
  print('X wins!')
else:
  print('Y wins!')

