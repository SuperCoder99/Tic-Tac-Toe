from Functions import *

board = [[None for _ in range(3)] for _ in range(3)]
player_number = 0

while(player_number <= 8):
  move = -1

  while(True):
    try:
      move = int(input("Enter Number from 1-9: ")) - 1 
      if not 0 <= move <= 8:
        print("Invalid Input. Enter Number in Range 1-9")
        continue         
      break
    except ValueError:
      print("Enter a valid Integer from 1-9")

  row = move // 3
  column = move % 3  

  if board[row][column] is not None :
    print("Invalid Input")
    continue

  board[row][column] = player_number % 2
  
  List_Display(board)
  Win(board, player_number)
  
  player_number += 1

if player_number == 9:
  print("Game Drawn!")
  exit()