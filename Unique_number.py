n=int(input())
t=n
rev=0
b=' '
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
    c=str(r)
    a=list(c)
    for i in c:
        if i not in b and c.count(i)==1:
            b+=i
d=int(b)
if(d==rev):
    print("Unique Number")
else:
    print("Not Unique Number")