n=int(input())
rev=0
c=0
s=0
i=1
t=n
while n>0:
    re=n%10
    rev=rev*10+re
    n=n//10
while rev>0:
    r=rev%10
    rev=rev//10
    c+=1
    while i<=c:
        s+=r**i
        i+=1
if s==t:
    print(True)
else:
    print(False)