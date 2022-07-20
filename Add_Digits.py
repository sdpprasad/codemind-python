n=int(input())
s=n
while(s>9 ):
    n=s
    s=0
    while(n>0):
        r=n%10
        s+=r
        n//=10
print(s)
