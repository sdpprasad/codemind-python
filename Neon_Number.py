n=int(input())
b=n*n
s=0
while b!=0:
    r=b%10
    s+=r
    b=b//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")
    