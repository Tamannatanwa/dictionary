a=[1,2,4,1,2,7,1,4]
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        c=a.count(a[i])
        if c==1:
            print(a[i])
    i=i+1

        
        
        
        