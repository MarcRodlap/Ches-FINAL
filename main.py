from replit import db

# Board is 8x8
def createBoard():
    dims=(8, 8)
    board = []
    for row in range(dims[0]):
        board.append([" "]*dims[1])
    board = assignPawns(board, "White")
    board = assignPawns(board, "Black")
    board = assignRest(board, "White")
    board = assignRest(board, "Black")
    return board
  
# Put pawns in row
def assignPawns(board, bw):
    if bw=="White":
        board[1] = ["♙","♙","♙","♙","♙","♙","♙","♙"]
    elif bw=="Black":
        board[6] = ["♟","♟","♟","♟","♟","♟","♟","♟"]
      
    return board

# Put other pieces in row
def assignRest(board, bw):
    if bw=="White":
        board[0] = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
    elif bw=="Black":
        board[7] = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
    return board
  
# From is a tuple of (x, y)
# To is a tuple of (x, y)
  
def movePiece(board, initial, final):
    Ls = ["♖", "♘", "♗", "♕", "♔","♙"]
    
    piece = board[initial[0]][initial[1]]
    board[initial[0]][initial[1]] = " "
    
    if board[final[0]][final[1]] in Ls:
      board[final[0]][final[1]] = " "
    
    board[final[0]][final[1]] = piece    
    return board

def movePiece(board, initial, final):
    LsW = ["♖", "♘", "♗", "♕", "♔","♙"]
    LsB = ["♜", "♞", "♝", "♛", "♚","♟"]
    piece = board[initial[0]][initial[1]]
    
    if board[initial[0]][initial[1]] in LsB:
      board[initial[0]][initial[1]] = " "
    
      if board[final[0]][final[1]] in LsW:
        board[final[0]][final[1]] = " "
    
      board[final[0]][final[1]] = piece    
      return board

    if board[initial[0]][initial[1]] in LsW:
      board[initial[0]][initial[1]] = " "
    
      if board[final[0]][final[1]] in LsB:
        board[final[0]][final[1]] = " "
    
      board[final[0]][final[1]] = piece    
      return board

def movePawn(board, bw, initial, final):
    legalMove = None
    if bw=="White":
        legalMove = 1
    elif bw=="Black":
        legalMove = -1
    if initial[0]+legalMove == final[0]:
        return movePiece(board, initial, final)
    else:
        print("Illegal Move")
        return board

def moveKnight(board, bw, initial, final):
  legalMove = [[1,2],[2,1],[-2,1],[2,-1],[-2,-1],[-1,-2],[-1,2],[1,-2]]
  w = len(legalMove)
  for i in range(len(legalMove)):
    print ("~")
    if initial[0]+legalMove[i][0] != final[0]:
        w = w -1
    
    if initial[1]+legalMove[i][1] != final[1]:
        w = w -1
        
    if initial[1]+legalMove[i][1] == final[1]:
        if initial[0]+legalMove[i][0] == final[0]:
          return movePiece(board, initial, final)

    if w == 0:
      print("Illegal Move")
      return board
   
    

  

def moveBishop(board, bw, initial, final):
  legalMove = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7]]
  w = len(legalMove)
  for i in range(len(legalMove)):
    print ("~")
    if initial[0]+legalMove[i][0] != final[0]:
        w = w -1
    
    if initial[1]+legalMove[i][1] != final[1]:
        w = w -1
        
    if initial[1]+legalMove[i][1] == final[1]:
        if initial[0]+legalMove[i][0] == final[0]:
          return movePiece(board, initial, final)

    if w == 0:
      print("Illegal Move")
      return board

def moveRook(board, bw, initial, final):
  if initial[0] == final[0]:
    if initial[1] != final[1]:
      return movePiece(board, initial, final)
    else:
      print("Illegal Move")
      return board
      
  if initial[0] != final[0]:
    if initial[1] == final[1]:
      return movePiece(board, initial, final)
    else:
      print("Illegal Move")
      return board
  
  

def moveKing(board, bw, initial, final):
  legalMove = [[1,2],[2,1],[-2,1],[2,-1],[-2,-1],[-1,-2],[-1,2],[1,-2]]
  w = len(legalMove)
  for i in range(len(legalMove)):
    print ("~")
    if initial[0]+legalMove[i][0] != final[0]:
        w = w -1
    
    if initial[1]+legalMove[i][1] != final[1]:
        w = w -1
        
    if initial[1]+legalMove[i][1] == final[1]:
        if initial[0]+legalMove[i][0] == final[0]:
          return movePiece(board, initial, final)

    if w == 0:
      print("Illegal Move")
      return board


def moveQueen(board, bw, initial, final):
  if initial[0] == final[0]:
    if initial[1] != final[1]:
      return movePiece(board, initial, final)
    else:
      print("Illegal Move")
      return board
      
  if initial[0] != final[0]:
    if initial[1] == final[1]:
      return movePiece(board, initial, final)
    else:
      print("Illegal Move")
      return board
      
  legalMove = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7]]
  w = len(legalMove)
  for i in range(len(legalMove)):
    print ("~")
    if initial[0]+legalMove[i][0] != final[0]:
        w = w -1
    
    if initial[1]+legalMove[i][1] != final[1]:
        w = w -1
        
    if initial[1]+legalMove[i][1] == final[1]:
        if initial[0]+legalMove[i][0] == final[0]:
          return movePiece(board, initial, final)

    if w == 0:
      print("Illegal Move")
      return board
  

board = createBoard()
for row in board:
    print(row)

placeX = int(input("input X coordinate of piece that you would like to move: "))
placeY = int(input("input Y coordinate tof piece that you would like to move: "))

movingX = int(input("input X coordinate that you would like to move to: "))
movingY = int(input("input Y coordinate that you would like to move to: "))

if board[placeY][placeX]== "♟":
  board = movePawn(board, "Black", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♞":
  board = moveKnight(board, "Black", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♝":
  board = moveBishop(board, "Black", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♜":
  board = moveRook(board, "Black", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♚":
  board = moveQueen(board, "Black", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♛":
  board = moveKing(board, "Black", (placeY, placeX), (movingY, movingX))

for row in board:
    print(row)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  
placeX = int(input("input X coordinate of piece that you would like to move: "))
placeY = int(input("input Y coordinate tof piece that you would like to move: "))

movingX = int(input("input X coordinate that you would like to move to: "))
movingY = int(input("input Y coordinate that you would like to move to: "))

if board[placeY][placeX]== "♙":
  board = movePawn(board, "White", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♘":
  board = moveKnight(board, "White", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♗":
  board = moveBishop(board, "White", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♖":
  board = moveRook(board, "White", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♔":
  board = moveQueen(board, "White", (placeY, placeX), (movingY, movingX))

if board[placeY][placeX]== "♕":
  board = moveKing(board, "White", (placeY, placeX), (movingY, movingX))


for row in board:
    print(row)















#save deleted code if needed here VVVVVV
'''
[":chess_pawn:",":chess_pawn:",":chess_pawn:",":chess_pawn:",":chess_pawn:",":chess_pawn:",":chess_pawn:",":chess_pawn:"]



'''