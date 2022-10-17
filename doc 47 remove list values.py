a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
b=list(a)
c=list(a.values())
i=0
x={}
while i<len(b):
    c[i].clear()
    x[b[i]]=c[i]
    i=i+1
print(x)
    
