n=int(input())
b=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if b[i]%2==0:
        es+=b[i]
    else:
        os+=b[i]
print(abs(es-os))
    