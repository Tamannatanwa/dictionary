a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
c=[]

i=0
while i<len(a):
    b={}
    for j in a[i]:
        b[j]=int(a[i][j])
    c.append(b)
    i=i+1
print(c)