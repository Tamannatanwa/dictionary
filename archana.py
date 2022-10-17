a=['A','B']
i=0
b=[]
while i<len(a):
    j=1
    while j<=5:
        b.append(a[i]+str(j))
        j=j+1
    i=i+1
print(b)