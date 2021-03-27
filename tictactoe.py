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

  def print_board(self):
    print(self.coords["1,1"]+"|"+self.coords["1,2"]+"|"+self.coords["1,3"])
    print(self.coords["2,1"]+"|"+self.coords["2,2"]+"|"+self.coords["2,3"])
    print(self.coords["3,1"]+"|"+self.coords["3,2"]+"|"+self.coords["3,3"])

def main():
  obj = Tictactoe()
  obj.print_board()

if __name__ == '__main__':
  main()
