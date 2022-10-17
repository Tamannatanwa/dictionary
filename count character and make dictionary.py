a="mississippi"
i=0
b=[]
x={}
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        c=a.count(a[i])
        x[a[i]]=c
    i=i+1
print(x)