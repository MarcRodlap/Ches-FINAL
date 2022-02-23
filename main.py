from replit import db

import sys

from art import tprint
import os
tprint("H O P C h e s s", "Boxing")
print("--by Lucas Garcia, Marcos Rodriguez-Lapido, Emilio Dibildox--\n\n")


import random

#grabs players name and randomly gives them dark or light pieces
darkPlayer = []
lightPlayer = []
select = []
def NameSelection():
  
  playerOne = input("input player 1 name: ")
  select.append(playerOne)
  playerTwo = input("input player 2 name: ")
  select.append(playerTwo)
  
  select.remove(random.choice(select))
  darkPlayer.append(select[0])
  
  if playerOne in darkPlayer:
    lightPlayer.append(playerTwo)
    print(playerOne + " is playing the dark pieces and going first")
    print(playerTwo + " is playing the light pieces and is going second")
  else:
    lightPlayer.append(playerOne)
    print(playerTwo + " is playing the dark pieces and going first")
    print(playerOne + " is playing thelight pieces and is going second")
    
 

  
  

# creates Board that is 8x8 
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

#the move piece function moves the piece to the players inputed location while also checking if it landed on an enemy piece to eat
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

#if you select to move a pawn this makes sure you only move what a pawn is capable of 
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

#if you select to move a knight this makes sure you only move what a knight is capable of 
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
   
#if you select to move a bishop this makes sure you only move what a bishop is capable of 
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

#if you select to move a rook this makes sure you only move what a rook is capable of
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
  
  
#if you select to move a king this makes sure you only move what a king is capable of 
def moveKing(board, bw, initial, final):
  legalMove = [[1,1],[1,-1],[-1,0],[0,-1],[0,1],[1,0],[-1,-1],[-1,1]]
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

#if you select to move a Queen this makes sure you only move what a Queen is capable of(combined bishop & rook checks)
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
  

#actual code VVVV



      
#creates/prints the board
board = createBoard()

#grabs players name and randomly gives them dark or light pieces
NameSelection()

#laying out grid of chess board important for player to know when they need to move
print("IMPORTANT")
print("keep in mind these are points of board:")
print(" + 0  |  1  |  2  |  3  |  4  |  5  |  6  |  7 \n 0 \n - \n 1\n -  \n 2\n -  \n 3\n -  \n 4\n -  \n 5\n -  \n 6\n -  \n 7 \n ")


while True:

  a = 8
  y = 8
  
  #win check for light
  for i in range (len(board)):
    if "♛" not in board[i]:
      y = y - 1
  
  if y == 0:
    print("game over")
    print("light wins")
    print("congrats " + lightPlayer[0])
    break
  
  print("Its " + darkPlayer[0] + " turn to move(DARK)")
  
  for row in board:
    print(row) 
    
  #asks you the X and y coordinate of what piece you wanna move
  placeX = int(input("input X coordinate of piece that you would like to move: "))
  placeY = int(input("input Y coordinate tof piece that you would like to move: "))
    
  #asks you where you want to move that piece
  movingX = int(input("input X coordinate that you would like to move to: "))
  movingY = int(input("input Y coordinate that you would like to move to: "))
    
  #stores all the moves of the game in txt.file database
  file1 = open("txt.file","a")
  L = ["darkPlayer moved " + board[placeY][placeX] + " from (" + str(placeX) + "," + str(placeY) +") to (" + str(movingX) + "," + str(movingY) +")" ] 
  file1.write("\n ~~~~~~~~~~ \n")
  file1.writelines(L)
  file1.close()

  #since dark moves first these if statements will check that you're moving a dark piece
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

  

  #win check for dark
  for i in range (len(board)):
    if "♕" not in board[i]:
      a = a - 1
  
  if a == 0:
    print("game over")
    print("dark wins")
    print("congrats " + darkPlayer[0])
    break

  print("Its " + lightPlayer[0] + " turn to move(LIGHT)")
  
  placeX = int(input("input X coordinate of piece that you would like to move: "))
  placeY = int(input("input Y coordinate tof piece that you would like to move: "))
  
  movingX = int(input("input X coordinate that you would like to move to: "))
  movingY = int(input("input Y coordinate that you would like to move to: "))

  
  file1 = open("txt.file","a")
  L = ["lightPlayer moved "+  board[placeY][placeX] + " from (" + str(placeX) + "," + str(placeY) +") to (" + str(movingX) + "," + str(movingY) +")" ] 
  file1.write("\n ~~~~~~~~~~ \n")
  file1.writelines(L)
  file1.close()

  
  #since light moves second these if statements will check that you're moving a light piece
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


#sets a barrier in textfile for a new games moves
file1 = open("txt.file","a")
file1.write("\n ~~~~~~~~~~~~~~~~~New Game~~~~~~~~~~~~~~~~~~ \n")
file1.close()
