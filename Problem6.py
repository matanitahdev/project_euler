"""

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

sumOfSquares = 0
for i in range(1, 101):
    sumOfSquares += i*i

squareOfSum = 0
for i in range(1, 101):
    squareOfSum += i
squareOfSum *= squareOfSum

print(squareOfSum - sumOfSquares)
