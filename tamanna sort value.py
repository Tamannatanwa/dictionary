# dt={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# v=list(dt.values())
# c=sorted(v)
# x={}
# j=0
# for k in dt:
#     x[k]=c[j]
#     j=j+1
# print(x)




dt=[{'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}]
i=0
while i<len(dt):
    x=dt[i]
    i=i+1
v=list(x.values())
c=sorted(v)
f={}
j=0
for k in x:
    f[k]=c[j]
    j=j+1
print([f])
