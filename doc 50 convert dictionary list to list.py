a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
b=list(a)
c=list(a.values())
i=0
x=[]
while i<len(b):
    j=0
    y=[]
    while j<1:
        y.append(b[i])
        y.append(c[i])
        j=j+1
    x.append(y)
    i=i+1
print(x)

        


