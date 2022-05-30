n=int(input())
f=0
for i in range(1,n//2+1):
    if(i*i==n):
        f=1
        break
if(f==1):
    print(True)
else:
    print(False)