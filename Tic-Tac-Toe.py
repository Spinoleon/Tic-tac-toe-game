board = [['1','2','3'],['4','X','6'],['7','8','9']]
from random import randrange

def displayboard(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+ board[0][0]+'   |   '+ board[0][1]+'   |   '+ board[0][2] +'   |')
    print('|       |       |       |')   
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+ board[1][0]+'   |   '+ board[1][1]+'   |   '+ board[1][2] +'   |')
    print('|       |       |       |')   
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+ board[2][0]+'   |   '+ board[2][1]+'   |   '+ board[2][2] +'   |')
    print('|       |       |       |')   
    print('+-------+-------+-------+')

def entermove(board):
    while True:
        try:
            move = int(input('Enter a number between (1-9): '))
        except ValueError:
            print('Please enter a valid number.')
            continue
            
        if move < 1 or move > 9:
            print('Sorry, you must enter a number between (1-9)')
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print('That space is occupied')
            continue
        
        for row in range(0,3):
            for column in range(0,3):
                if board[row][column] == str(move):
                    board[row][column] = '0'
          
        break

def listofFreeSpaces(board):
    global free_spaces
    free_spaces = []
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == 'X' or board[row][column] == '0':
                pass
            else:
                # FIX 1: Appended as standard coordinate tuple
                free_spaces.append((row, column)) 
    return free_spaces
      
def victoryfor(board , sign):
    print('Checking if there is a winner')
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        print('We DO NOT have a winner yet!!!')
        return False
    
def drawmove(board):
    while True:
        row = randrange(3)
        column = randrange(3)
  	    
        # FIX 2: Check if coordinates (row, column) are in the free_spaces list
        if (row, column) not in free_spaces:
            continue
        else:
            board[row][column] = 'X'
            return
  
human = '0'
computer = 'X'
numberofmoves = 1

print('Welcome to the Tic-Tac-Toe made in python!!!')
displayboard(board)

# Initialize free_spaces before the loop starts
listofFreeSpaces(board) 

while numberofmoves < 9:
    entermove(board)
    numberofmoves += 1
    displayboard(board)
    listofFreeSpaces(board)
    
    if victoryfor(board, human) == True:
        print('You are the winner')
        break
    
    # Prevent computer from trying to move if board is full
    if len(free_spaces) == 0:
        break
        
    print('Now the computers turn')
    drawmove(board)
    numberofmoves += 1
    
    # FIX 3: displayboard instead of display
    displayboard(board) 
    listofFreeSpaces(board)
        
    if victoryfor(board, computer) == True:
        print('The computer beat you, try again')
        break
        
else:
    print('We have a tie')
  
print('Thank you for playing')