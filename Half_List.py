n=int(input())
m=list(map(int,input().split()))
li=[]
li1=[]
for j in range(0,n//2):
    li1.append(m[j])
li=m[-1:-((n//2)+1):-1]
print(*(li+li1))