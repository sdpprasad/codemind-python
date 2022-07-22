n=int(input())
a=list(map(int,input().split()))
s=0
d=0
for i in a:
    s+=i
b=s//n
for j in a:
    if j==b:
        d+=1
if d==0:
    print(False)
else:
    print(True)