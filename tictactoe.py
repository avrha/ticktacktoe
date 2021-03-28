#!/usr/bin/python3

class Tictactoe():
  def __init__(self):
    self.values = [' ' for x in range(9)]
    self.player_pos = {'X': [], 'O':[]}
    self.current_player = 'X'

  def print_board(self):
    print("\n")
    print("\t1    |2    |3")
    print("\t  {}  |  {}  |  {}".format(self.values[0], self.values[1], self.values[2]))
    print('\t_____|_____|_____')
    print("\t4    |5    |6")
    print("\t  {}  |  {}  |  {}".format(self.values[3], self.values[4], self.values[5]))
    print('\t_____|_____|_____')
    print("\t7    |8    |9")
    print("\t  {}  |  {}  |  {}".format(self.values[6], self.values[7], self.values[8]))
    print("\t     |     |")
    print("\n")
  
  def single_game(self):

    if self.choose_mode():
      while True:
        print("Player Turn:", self.current_player)
        self.print_board()
        self.player_move()

        if self.check_win(): 
          self.print_board()
          print(self.current_player,"Wins!")
          break
        
        if self.check_tie():
          self.print_board()
          print("Tie Game!")
          break

        self.switch_turns()
    else:
      break 
      
      
  def player_move(self):
    while True:
      try:
        move = int(input("Enter Box Number (1-9): "))
      except:
        print("Value Error. Try again.")
        continue

      if move < 1 or move > 9:
        print("Incorrect Range. Try again.")
        continue

      if self.values[move-1] != ' ':
        print("Place already filled. Try again.")
        continue
      
      self.values[move-1] = self.current_player
      self.player_pos[self.current_player].append(move)
      break
  
  def switch_turns(self):
    if self.current_player == 'X':
      self.current_player = 'O'
    elif self.current_player == 'O':
      self.current_player = 'X'
    else:
      print("Switching error")
  
  def check_win(self):
    #Possible Winning cominbations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for i in range(7):
      tmp = []
      for j in range(3):
        for k in self.player_pos[self.current_player]:
          if soln[i][j] == k:
            tmp.append(k)
      
      if len(tmp) == 3:
        return True
    return False
            
  def check_tie(self):
    if len(self.player_pos['X']) + len(self.player_pos['O']) == 9:
      return True
    else:
      return False 

  def choose_mode(self):
    mode = input("Choose a game mode (PvP PvC): ")
   
    if mode.lower() == "pvp":
      return True
    
    elif mode.lower() == "pvc": 
      return False
      
    else:
      print("Invalid input, try again.")
      self.choose_mode(self)

def main():
  obj = Tictactoe()
  obj.single_game()

if __name__ == '__main__':
  main()
