a={"python":[45,25,30],"lan":[45,100,80],"py":[40,60,90],"with":[30,50,70]}
x=[]
for i in a:
    x.append(a[i])
i=0
z=[]
while i<3:
    j=0
    sum=0
    while j<len(x):
        sum+=x[j][i]
        j=j+1
    i=i+1
    z.append(sum)
print(z)