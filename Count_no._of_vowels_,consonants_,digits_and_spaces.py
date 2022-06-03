n=input()
v=0
c=0
d=0
w=0
for i in n:
    if i in 'aeiou':
        v+=1
    if i.isalpha() and i not in 'aeiou':
        c+=1
    if i in '0123456789':
        d+=1
    if i in ' ':
        w+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)