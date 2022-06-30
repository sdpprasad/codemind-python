n=int(input())
s1=[]
s2=[]
arr=list(map(int,input().split()))
for i in arr:
    if i==1:
        s1.append(1)
    elif i==0:
        s2.append(0)
print(*(s2+s1))