n=input()
while True:
    rev=n[::-1]
    x=int(n)+int(rev)
    x1=str(x)
    if x1==x1[::-1]:
        print(x)
        break
    n=x1