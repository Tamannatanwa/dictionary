num={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max=0
smax=0
sum={}
for i in num:
    if max<num[i]:
        max=num[i]
    elif smax<num[i]:
        smax=num[i]
b=[]
for j in num:
    if num[j]==max:
        b.append(j)
    elif num[j]==smax:
        b.append(j)
print(b)