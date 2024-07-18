"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

triplets = []
def pythagorean_triplet(n):
  for b in range(n):
    for a in range(1, b):
        c = math.sqrt( a * a + b * b)
        if c % 1 == 0:
            triplets.append(a)
            triplets.append(b)
            triplets.append(c)

pythagorean_triplet(10000)
for i in range(0, len(triplets), 3):
    if(triplets[i] + triplets[i+1] + triplets[i+2] == 1000):
        print(f"{triplets[i] * triplets[i+1] * triplets[i+2]}")
