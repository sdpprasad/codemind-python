n=int(input())
a=list(map(int,input().split()))
m=int(input())
c=0
for i in a:
    if(i==m):
        c+=1
if c==0:
    print(0)
else:
    print(c)