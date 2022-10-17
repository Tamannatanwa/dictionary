x=int(input("enter the length..."))
a=[]
i=0
count=0
z=[]
while i<x:
    c=int(input("enter the number.."))
    a.append(c)
    if a[i] not in z:
        z.append(a[i])
        pass
    else:
        count+=1
    i=i+1
print(z)
print(count)