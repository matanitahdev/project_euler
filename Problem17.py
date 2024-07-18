"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,342
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters.The use of "and" when writing
out numbers is in compliance with British usage.
"""
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight",
"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
"seventeen", "eighteen", "nineteen"]

def lessThanHundred(i):
    if(i < 20):
        return numbers[i-1]
    elif(i >= 20 and i < 30):
        if(i==20): return "twenty"
        return "twenty " + numbers[i % 10 -1]
    elif(i >= 30 and i < 40):
        if(i==30): return "thirty"
        return "thirty " + numbers[i % 10 -1]
    elif(i >= 40 and i < 50):
        if(i==40): return "forty"
        return "forty " + numbers[i % 10 -1]
    elif(i >= 50 and i < 60):
        if(i==50): return "fifty"
        return "fifty " + numbers[i % 10 -1]
    elif(i >= 60 and i < 70):
        if(i==60): return "sixty"
        return "sixty " + numbers[i % 10 -1]
    elif(i >= 70 and i < 80):
        if(i==70): return "seventy"
        return "seventy " + numbers[i % 10 -1]
    elif(i >= 80 and i < 90):
        if(i==80): return "eighty"
        return "eighty " + numbers[i % 10 -1]
    elif(i >= 90 and i < 100):
        if(i==90): return "ninety"
        return "ninety " + numbers[i % 10 -1]

def numberString(i):
    if(i < 100):
        return lessThanHundred(i)
    elif(i < 1000):
        string = numbers[i // 100 -1] + " hundred"
        if(i % 100 > 0):
            string += " and " + lessThanHundred(i % 100)
        return string
    else:
        return "one thousand"

sum = 0
for i in range(1,1001):
    print(i, ": ", numberString(i), len(numberString(i).replace(" ", "")))
    sum += len(numberString(i).replace(" ", ""))
print(sum)
