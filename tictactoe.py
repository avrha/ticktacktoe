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

  #def start_game(self):
    

  def print_board(self):
    print("  1 2 3")
    print("1 "+self.coords["1,1"]+"|"+self.coords["1,2"]+"|"+self.coords["1,3"])
    print("2 "+self.coords["2,1"]+"|"+self.coords["2,2"]+"|"+self.coords["2,3"])
    print("3 "+self.coords["3,1"]+"|"+self.coords["3,2"]+"|"+self.coords["3,3"])
    self.player_move()

  def player_move(self):
    move = input("Move (x,y): ")
    print(move)

    for i in self.coords: 
      if move == i:
        self.coords[i] = self.player_turn()
        self.print_board()

  def player_turn(self):
    if self.player1 == True:
      return "X"
    
    if self.player2 == True:
      return "O"
    
def main():
  obj = Tictactoe()
  obj.print_board()

if __name__ == '__main__':
  main()
