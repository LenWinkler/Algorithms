#!/usr/bin/python

import argparse

def find_max_profit(prices):
  
  current_i = 0
  proceed = True

  # using for loop, and starting i at prices[0], subtract price from each subsequent item in the list
  while proceed:
    # keep track of current_min_price_so_far, max_profit_so_far, and current index
    current_min_price_so_far = prices[0]
    max_profit_so_far = prices[1] - prices[0]

    if current_i == len(prices) - 1 and prices[current_i] - current_min_price_so_far > max_profit_so_far:
      max_profit_so_far = prices[current_i] - current_min_price_so_far
    for price in prices:
      j = current_i + 1
      diff = prices[j] - prices[current_i]

  # each time, the current result is compared to max_profit_so_far. if result > max, set max to result
      if diff > max_profit_so_far:
        max_profit_so_far = diff

  # move j to the right
      j += 1

  # when j reaches end of list, move current_i to the right



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))