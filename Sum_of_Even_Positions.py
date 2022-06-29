n=int(input())
b=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if i%2==0:
        es+=b[i]
print(es)