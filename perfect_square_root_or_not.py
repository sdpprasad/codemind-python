import math
n=int(input())
c=round(math.sqrt(n),2)
if(n==c*c):
    print(True)
else:
    print(False)