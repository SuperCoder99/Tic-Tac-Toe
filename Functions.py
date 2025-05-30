def List_Display(arr):
  symbols = {None: " ", 0: "X", 1: "O"}
  for row in arr:
      print(" | ".join(symbols[cell] for cell in row))
      print("-" * 9)

def Win(arr, Player_Number):
   
  winning_combinations = [
      [(0, 0), (0, 1), (0, 2)],
      [(1, 0), (1, 1), (1, 2)],
      [(2, 0), (2, 1), (2, 2)],
      
      [(0, 0), (1, 0), (2, 0)],
      [(0, 1), (1, 1), (2, 1)],
      [(0, 2), (1, 2), (2, 2)],
      
      [(0, 0), (1, 1), (2, 2)],
      [(0, 2), (1, 1), (2, 0)]
  ]   
  symbols = {None: " ", 0: "X", 1: "O"}

  for combo in winning_combinations:
    #access winning combinations to tally if such a combo is present and if all moves on the combo are same (O or X)
    a, b, c = combo
    if arr[a[0]][a[1]] == arr[b[0]][b[1]] == arr[c[0]][c[1]] is not None:
      print(f"Player {symbols[Player_Number % 2]} wins the Game!")
      exit()