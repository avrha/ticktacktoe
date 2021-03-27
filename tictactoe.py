#!/usr/bin/python3
import numpy as np

board_coords = np.array([[1,2,3],[1,2,3],[1,2,3]])

def print_board():
  print(" X    0     1     2")
  for i in range(0,3):
    if i == 0:
      print(
        "Y  |-----|-----|-----|\n"
        "   |     |     |     |\n",i,
        "|     |     |     |\n"
        "   |     |     |     |\n"
        "   |-----|-----|-----|"
        )
    else:
      print(
        "   |     |     |     |\n",i,
        "|     |     |     |\n"
        "   |     |     |     |\n"
        "   |-----|-----|-----|"
        )
      
if __name__ == '__main__':
  print_board()
