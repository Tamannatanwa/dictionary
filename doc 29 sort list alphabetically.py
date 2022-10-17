dt=[{'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}]
x={}
i=0
while i<len(dt):
    for j in dt[i]:
        x[j]=dt[i][j]
    i=i+1
y=sorted(x.items())
print(dict(y))
    



dt={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
v=list(dt.values())
c=sorted(v)
x={}
j=0
for k in dt:
    x[k]=c[j]
    j=j+1
print(x)