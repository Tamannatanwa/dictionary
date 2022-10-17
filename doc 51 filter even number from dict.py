x={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
y=list(x)
z=list(x.values())
i=0
r=dict()
while i<len(y):
    j=0
    v=[]
    while j<len(z[i]):
        if z[i][j]%2==0:
            v.append(z[i][j])
        j=j+1
    r[y[i]]=v
    i=i+1
print(r)
        