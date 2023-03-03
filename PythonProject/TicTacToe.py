 #define the board
board = [["_" for i in range(3)] for j in range(3)]

# Improvement #1: Changed inputs from 0-2 to 1-3. Makes it more intuitive to input rows and columns.
# Improvement #2: Cannot overwrite an existing placement of an X or O. If tried, will not accept and must place elsewhere, turn will not continue until placed properly.
# Improvement #3: At the start of a turn, states which player's turn it is. 

# define the player's move
def make_move(board, player, row, col):
  row = row-1 #Improvement #1. Input 1-3 changed to input-1 (0-2), which the code already works with.
  col = col-1 #Improvement #1.
  if board[row][col] == "_": # Improvement #2. Can only place an X or O on an "empty" spot.
      board[row][col] = player

# define the function to check for a winner
def check_winner(board):
  # check rows
  for row in range(3):
    if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
      return board[row][0]

  # check columns
  for col in range(3):
    if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
      return board[0][col]

  # check diagonals
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
    return board[0][0]
  if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
    return board[2][0]

  # if there is no winner, return None
  return None

# define the function to check if the game is a draw
def check_draw(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == "_":
        return False
  return True

# define the function to play the game
def play_game():
  # initialize the game
  player = "X"
  winner = None
  draw = False

  # loop until the game is over
  while not winner and not draw:
    print("It is player", player, "'s turn.'") # Improvement #3. States which player's turn it is. Corresponds to improvement #2, always know if it's still your turn after making an 'illegal' play. 
    # print the current board
    for row in board:
      print(" ".join(row))

    # get the player's move
    row = int(input("Enter row (1-3): "))
    col = int(input("Enter column (1-3): "))

    # make the move
    make_move(board, player, row, col)

    # check for a winner
    winner = check_winner(board)

    # check for a draw
    draw = check_draw(board)

    # switch players
    if player == "X" and board[row-1][col-1] == "X": # Improvement #2. Player only switches when an the corresponding symbol is placed on an "empty" spot, otherwise, player does not change until this is done.
      player = "O"
    elif player == "O" and board[row-1][col-1] == "O": # Improvement #2. 
      player = "X"

  # print the final board
  for row in board:
    print(" ".join(row))

  # print the result of the game
  if winner:
    print(f"Player {winner} wins!")
  else:
    print("The game is a draw.")
    
# play the game
play_game()
