"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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


notFound = True
i = 2
count = 1
while(notFound):
    i += 1
    if(isPrime(i)):
        count += 1
    if(count == 10001):
        notFound = False


print(i)
