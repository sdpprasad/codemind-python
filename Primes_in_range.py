def prime(num):
    if num==1:
        return False
    else:    
        for j in range(2,int(num**0.5)+1):
            if num%j==0:
                return False
        else:
        
            return True


n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if prime(i):
        c+=1
print(c)