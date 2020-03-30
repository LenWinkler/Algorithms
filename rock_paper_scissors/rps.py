#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  
  # 
  plays = ['rock', 'paper', 'scissors']
  possible_plays = []

  # should return empty list if 0 is passed in
  if n == 0:
    return [possible_plays]
  # passing in 1 returns [[rock], [paper], [scissors]]
  elif n == 1:
    for play in plays:
      possible_plays.append([play])
    return possible_plays
  
    

"""[['rock', 'rock'], ['rock', 'paper'],['rock', 'scissors'], 

   ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], 

   ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]"""

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')