"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""
numStr = str(2**1000)
sum = 0
for c in numStr:
    sum += ord(c) - ord('0')
print(sum)
