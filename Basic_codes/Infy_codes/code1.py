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
#print(res)
print(min(res))


# input
#n=16
#s=0000111100001110

#output 
#1