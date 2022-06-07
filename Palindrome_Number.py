t=int(input())
for i in range(t):
    n=int(input())
    re=0
    te=n
    while n>0:
        r=n%10
        re=re*10+r
        n=n//10
    if te==re:
        print(True)
    else:
        print(False)