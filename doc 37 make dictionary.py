x={}
i=11
a=[]
b=[]
c=[]
while i<40:
    if i>10 and i<20:
        a.append(i)
    elif i>20 and i<30:
        b.append(i)
    elif i>30 and i<40:
        c.append(i)
    i=i+1
x["x"]=a
x["y"]=b
x["z"]=c
print(x)
        