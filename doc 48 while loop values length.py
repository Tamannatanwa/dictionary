dict={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
x=list(dict.values())
i=0
z={}
while i<len(x):
    z[x[i]]=len(x[i])
    i=i+1
print(z)
    
    

