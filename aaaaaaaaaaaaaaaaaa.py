def prime(num):
    if num==1:
        return False
    else:    
        for j in range(2,int(num**0.5)+1):
            if num%j==0:
                return False
        else:
        
            return True
k=int(input())
c=0
if k==1:
    print(1)
else:    
    for j in range(2,int(k**0.5)+1):
        if k%j!=0:
            c+=1
print("prime")
n=2##n=int(input())
m=k##m=int(input())
a1=[]
max=k
c=0
for i in range(n,m+1):
    if prime(i):
        #c+=1
        #print(i)
        a1.append(i)
##print(a1)
for i in a1:
##    print(i)
    for j in a1:
        if(i+(j+1)==k):
            sum=i+(j+1)
##            //print(sum)
            if(sum<=max):
                max=sum
                #print(i)
                #print(j+1)
                p1=i
                p2=j+1
print(p1)
print(p2)
