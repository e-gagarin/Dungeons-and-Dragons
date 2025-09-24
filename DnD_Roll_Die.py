import random

def roll_die(sides):
  """Return a random integer from 1 to 'sides' (inclusive)."""
  #Input validation
  if not isinstance(sides, int) or sides < 1:
    raise ValueError("sides must be a positive integer")

  #Do the roll
  return random.randint(1, sides)

print(roll_die(6))   # should give 1–6
print(roll_die(20))  # should give 1–20
