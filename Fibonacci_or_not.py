n=int(input())
flag=0
a=0
b=1
s=[]
for i in range(0,n+1):
    s.append(a)
    c=a+b
    a=b
    b=c
if n in s:
    print(True)
else:
    print(False)