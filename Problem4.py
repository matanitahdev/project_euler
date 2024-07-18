"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
def isPalindrome(n):
    string = str(n)
    if(string == string[::-1]):
        return True
    else:
        return False

i=100
max = 101
while(i<999):
    j=100
    while(j<999):
        j+=1
        product = i*j
        if(isPalindrome(product)):
            if(product > max):
                max = product
    i+=1


print(max)
