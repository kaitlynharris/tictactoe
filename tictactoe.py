import re

def newBoard():
    # Define blank list
    board = []
    #Generate rows with length of 3
    for row in range(4):
      # Append a blank list to each row cell
      board.append([])
      for column in range(4):
        # Assign x to each row
        board[row].append('-')

    # Add coordinate labels
    board[0][0] = " "
    board[0][1] = "A"
    board[0][2] = "B"
    board[0][3] = "C"
    board[1][0] = "1"
    board[2][0] = "2"
    board[3][0] = "3"

    return board

def printBoard(board):
    for row in board:
        print " ".join(row)

def getColumn():
    column = raw_input("Choose a column: ").upper()
    if re.match(r'[ABC]', column) is not None:
        horizontalGuide = {"A":1, "B": 2, "C":3}
        column = horizontalGuide[column]
        return column
    else:
        print "Please choose A, B, or C"
        return getColumn()

def getRow():
    row = raw_input("Now choose a row: ")
    if re.match(r'[123]', row) is not None:
        return int(row)
    else:
        print "Please choose 1,2, or 3"
        return getRow()

def checkMove(board, row, column):
    if board[row][column] == '-':
        return True
    else:
        return False

def makeMove(board, column, row, player):
    board[row][column] = player

def verifyMove(player, board, row, column):
    if checkMove(board, row, column):
        print("You have chosen to place your {} at {},{}".format(player,column,row))
        makeMove(board, column, row, player)
        printBoard(board)
        if checkWin(player, board):
            endGame(player, board)
        else:
            player = switchPlayer(player)
            #changed move() to catGame()
            return catGame(player, board)
    else:
        print "This space is already taken"
        #changed move() to catGame()
        return catGame(player, board)

#added catGame code
def catGame(player, board):
    cat=[]
    for row in range(4):
        if (board[row][1] == '-' or board[row][2] == '-' or board[row][3] == '-'):
            cat.append("nocat")
        else:
            cat.append("catgame")
    if ("nocat" in cat):
        move(player, board)
    else:
        print("CAT'S GAME")
        endGame(player, board)
        

def move(player, board):
    print("Player {}, please make your move".format(player))
    column = getColumn()
    row = getRow()
    verifyMove(player, board, row, column)

def switchPlayer(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return player

def checkWin(player, board):
   for column in range(4):
       if board[1][column] == player:
           if (board[2][column] == player and board[3][column]==player):
               print("Player {} has won".format(player))
               return True
   for row in range(4):
       if board[row][3] == player:
           if (board[row][2]==player and board[row][1]== player):
               print ("Player {} has won".format(player))
               return True
   if (board[2][2]== player):
       if (board[1][1]==player and board[3][3]==player):
           print ("Player {} has won".format(player))
           return True
       elif (board[1][3]== player and board[3][1]==player):
           print ("Player {} has won".format(player))
           return True
   else:
       return False

def endGame(player, board):
    again = raw_input("Would you like to play again? y/n ")
    if (again.lower() == "y" or  again.lower() == "yes"):
       print("Let's play another game")
       board = newBoard()
       printBoard(board)
       player = switchPlayer(player)
       return move(player, board)
    elif (again.lower() == "n" or again.lower() == "no"):
       print("It was nice playing with you.")
       exit()
    else:
       print("Please answer yes or no")
       return endGame()
    return

def main():
    player = "X"
    board = newBoard()
    print "Welcome to Tic Tac Toe"
    printBoard(board)
    catGame(player, board)
    #move(player, board)

if __name__ == '__main__':
    main()
