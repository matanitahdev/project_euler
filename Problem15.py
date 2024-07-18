"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

I solved this problem with a simple binomial coefficient; 40 choose 20. This is the number of ways
to arrange 40 elements into groups of 20, which has a one to one correspondence to the 20 steps which must go
down and the 20 steps which must go right. Thus our answer was 137846528820.
"""
