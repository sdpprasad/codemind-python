n=int(input())
c=0
while n>0:
    r=n%10
    n=n//10
    c+=1
if c<10 or r==0:
    print("Invalid")
else:
    print("Valid")