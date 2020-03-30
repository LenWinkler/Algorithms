#!/usr/bin/python

import argparse

def find_max_profit(prices):

  # loop through prices and find cheapest price that has items to the right of it
  # set lowest price to variable
  current_min_price_so_far = None
  max_profit_so_far = -2000000000
  for i in range(0, len(prices) - 1):
    if current_min_price_so_far == None:
      current_min_price_so_far = prices[i]
    elif prices[i + 1] and prices[i] < current_min_price_so_far:
      current_min_price_so_far = prices[i]
  
  my_prices = prices[prices.index(current_min_price_so_far) + 1 : ]

  # subtract cheapest price from all prices to the right of it
  for price in my_prices:
    if price - current_min_price_so_far > max_profit_so_far:
      max_profit_so_far = price - current_min_price_so_far

  # set largest difference to variable
  # return largest difference
  return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))