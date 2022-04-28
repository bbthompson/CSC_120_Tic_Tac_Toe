# Create board (list of 3 lists)
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


# Function to print board
def print_board():
    print("Printing board...")
    for i in range(len(board)):
        print(board[i])


# Function to check for valid mark
def check_mark(row, col):
    # Check to make sure that the row and column entered by user are 0-2
    if ((row < 0) or (row > 2)) or ((col < 0) or (col > 2)):
        print("**** Invalid row or column. ****")
        print("**** Please select row/column values 0 to 2. ****")
        return False
    else:
        # Check to make sure that the row and column entered by the user has not been taken
        if board[row][col] == "-":
            return True
        else:
            print("**** Board space ["+str(row)+"],["+str(col)+"] has already been selected. Please select somewhere else on the board ****")
            print("**** Invalid choice. Please mark again ****")
            return False


# Function to place a mark on the board. Player 1 will make an "X". Player 2 will make an "O"
def place_mark(row, col, playerId):
    if playerId == 1:
        board[row][col] = "X"
    else:
        board[row][col] = "O"


# Function to check for win
def check_win(playerId):
    win = False
    # Check rows and columns for win
    for i in range(len(board)):
        # Check for 3 in a row horizontally
        if (board[i][0] != "-") and (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]):
            win = True
        # Check for 3 in a row vertically
        elif (board[0][i] != "-") and (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]):
            win = True
    # Check diagonals for win
    if board[0][0] != "-" and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        win = True
    elif board[0][2] != "-" and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        win = True
    return win


# Set number of marked spaces on board to 0, maximum marks to 9, player id to 1, and win to False
MAXMARKS = 9
playerId = 1
markCount = 0
win = False

# While board is not filled, allow players to make marks
while markCount < MAXMARKS:
    # Print the board
    print_board()
    # Prompt player for row and columns for their move
    print("Player", playerId, "make your move")
    row = int(input("Enter row number(0-2): "))
    col = int(input("Enter col number(0-2): "))
    # Validate the entered row and column
    if not check_mark(row, col):
        continue
    # Place the mark in the row and column on the board for the player
    place_mark(row, col, playerId)
    # Check for win/Exit loop if game is over
    if check_win(playerId):
        print_board()
        print("Player ", playerId, "wins! Game over!")
        win = True
        break
    # Switch players
    if playerId == 1:
        playerId = 2
    else:
        playerId = 1
    markCount = markCount + 1


# Check for a draw
if markCount == 9 and win == False:
    print_board()
    print("It's a draw!")


