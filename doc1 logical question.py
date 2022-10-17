a={'a':100,'b':200,'c':300}
b={'a':300,'b':200,'d':400}
i=0
x=list(a)
y=list(b)
c=list(a.values())
d=list(b.values())
z={}
while i<len(a):
    if x[i]==y[i]:
        sum=c[i]+d[i]
        z[x[i]]=sum
    else:
        z[x[i]]=c[i]
        z[y[i]]=d[i]
    i=i+1
print(z)
        
    
    
  