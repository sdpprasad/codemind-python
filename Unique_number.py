a=input()
le=len(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
le2=len(b)
if le==le2:
    print("Unique Number")
else:
    print("Not Unique Number")
