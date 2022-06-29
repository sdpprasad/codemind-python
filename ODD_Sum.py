n=int(input())
b=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if b[i]%2!=0:
        os+=b[i]
print(os)