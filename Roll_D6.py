import random

def roll_six_sided_die():
      """Sims rolling a six sided die and returns result"""
      return random.randint(1, 6)

result = roll_six_sided_die()
print(f"You rolled a {result}!")
      
# Receiving a syntax error on line 8 that parantheses weren't closed - I had it as (f"You rolled a {result})!", totally valid error
# Code works but dice isn't being rolled at random, rolling 1-4 in order.
# Disregard previous comment, results are definitely randomized it just so happens that it rolled in sequence, 1 in 1,296 odds of that happening
