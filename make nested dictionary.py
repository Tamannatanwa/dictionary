i=0
v={}
s=["aniket","RAM","priya","amrita"]
while i<5:
    j=0
    b=[]
    x={}
    while j<i:
        y=int(input("enter the number....."))
        b.append(y)
        j=j+1
    x[s[j]]=b
    v["RAM"]=x
    i=i+1
print(v)