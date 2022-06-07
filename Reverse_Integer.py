n=int(input())
rev=0
if n<0:
    n=n*-1
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    print(rev*-1)
else:
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    print(rev)