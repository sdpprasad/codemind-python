import math
n=int(input())
b=round(math.sqrt(n),2)
if b*b==n:
    print(True)
else:
    print(False)