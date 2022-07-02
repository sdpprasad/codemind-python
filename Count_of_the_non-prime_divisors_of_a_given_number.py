def prime(num):
    if num==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return False
    return True
    
n=int(input())
p_div=div=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i):
            p_div+=1
        div+=1
print(div-p_div)
    