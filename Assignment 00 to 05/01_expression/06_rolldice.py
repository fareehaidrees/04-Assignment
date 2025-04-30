"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
import random

num_sides: int = 6

def main():
    random.seed(1)
    
    die1: int = random.randint(1, num_sides)
    die2: int = random.randint(1, num_sides)
    total: int = die1 + die2
    
    print("Dice have", num_sides, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()