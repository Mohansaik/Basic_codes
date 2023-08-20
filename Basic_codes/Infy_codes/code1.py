'''
*** K-switchings ***

A string it contains 0 or 1.
you have make minimum changes based on below conditions.
    1. if you consider substring len k that should be divisible of N (len of string)
    2. the switchings should follow particular pattern example if k=2 then 
       string should be like 00 11 00 11 00 and soon.

Sample Input:

N=16
S='0000111100001110'

Sample Output:
1

'''


def find_factors(number):
    factors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    return factors

n=int(input())
s=input()
factors=find_factors(n)
res=[]

for i in factors:
    count=0
    if i !=1:
        ref=1
        for j in range(i,n+1,i):
            if ref%2!=0:
                count+=s[j-i:j].count('1')
                ref+=1
            else:
                count+=s[j-i:j].count('0')
                ref-=1
        res.append(count)
print(min(res))