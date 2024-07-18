"""
Find the sum of all the primes below two million.
"""
def isPrime(n):
    if n == 1:
        return False
    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            return False
        i += 1
    return True

sum=0
for i in range(2000000):
    if(isPrime(i)):
        sum+=i


print(sum)
