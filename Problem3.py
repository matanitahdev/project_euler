"""
What is the largest prime factor of the number 600851475143 ?
"""
import math

n = 600851475143
max=0

for i in range(3,int(math.sqrt(n))):

        # while i divides n , print i and divide n
    while n % i== 0:
        if(i>max):
            max=i
        n = n / i

print(max)
