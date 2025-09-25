import random

def roll_die(sides):
  """Return a random integer from 1 to 'sides' (inclusive)."""
  #Input validation
  if not isinstance(sides, int) or sides < 1:
    raise ValueError("sides must be a positive integer")

  #Do the roll
  return random.randint(1, sides)

def roll_dice(count, sides):
    """Roll 'count' dice with 'sides' sides. Returns (list_of_rolls, total)."""
    results = []  # store each roll here

    for i in range(count):
        roll = roll_die(sides)
        results.append(roll)

    total = sum(results)
    return results, total
