n=int(input())
s=0
p=1
while(n!=0):
    r=n%10
    p*=r
    s+=r
    n=n//10
if p>s:
    print(p-s)
else:
    print(s-p)
    