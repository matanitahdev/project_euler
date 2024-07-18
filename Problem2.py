"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
def fibb(n):
    if(n==0):
        return 1
    elif(n==1):
        return 2
    else:
        return fibb(n-2)+fibb(n-1)
i=0
sum=0
x=0
while x < 4000000 :
    x=fibb(i)
    i+=1
    if(x % 2 ==0):
        sum+=x
print(sum)
