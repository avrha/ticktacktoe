#!/usr/bin/python3

class Tictactoe():
  def __init__(self):
    self.values = [' ' for x in range(9)]
    self.player_pos = {'X': [], 'O':[]}

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

def main():
  obj = Tictactoe()
  obj.print_board()

if __name__ == '__main__':
  main()
