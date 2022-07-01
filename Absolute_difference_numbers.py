a,b=map(int,input().split())
st=str(a)
s1=st[0:b]
s2=st[len(st)-b:len(st)+1]
print(abs(int(s1)-int(s2)))