#!/usr/bin/python3


class Tictactoe:
  def __init__(self):
    self.coords = {
     "1,1": "-",
     "1,2": "-",
     "1,3": "-",
   
     "2,1": "-",
     "2,2": "-",
     "2,3": "-",
   
     "3,1": "-",
     "3,2": "-",
     "3,3": "-"
    } 

    self.player1 = True
    self.player2 = False

  def start_game(self):
    print("Welcome to tic tac toe!")
    self.choose_mode()
    
    while True:
      self.print_board()
      self.player_move()

    
  def choose_mode(self):
    game_mode = input("Choose game mode: PvP or PvC: ")
    if game_mode.lower() == "pvp":
      print("pvp test")
    elif game_mode.lower() == "pvc":
      print("pvc test")
    else:
      print("Invalid option, try again")
      self.choose_mode()

    
  def print_board(self):
    print("  1 2 3")
    print("1 "+self.coords["1,1"]+"|"+self.coords["1,2"]+"|"+self.coords["1,3"])
    print("2 "+self.coords["2,1"]+"|"+self.coords["2,2"]+"|"+self.coords["2,3"])
    print("3 "+self.coords["3,1"]+"|"+self.coords["3,2"]+"|"+self.coords["3,3"])


  def player_move(self):
    move = input("Move (x,y): ")
    print(move)
    x = "X"
    o = "O"
    
    if self.player1 == True:
      for i in self.coords: 
        if move == i:
          self.coords[i] = x

      self.player1 = False
      self.player2 = True

    elif self.player2 == True:
      for i in self.coords: 
        if move == i:
          self.coords[i] = o

      self.player1 = True
      self.player2 = False
      

def main():
  obj = Tictactoe()
  obj.start_game()

if __name__ == '__main__':
  main()
