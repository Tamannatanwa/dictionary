dt={1:2,3:4,4:3,2:1,0:0}
c=sorted(dt.items())
x=dict()
for i in c:
    num=list(i)
    j=0
    while j<len(num)-1:
        x[num[j]]=num[j+1]
        j=j+1
print(x)
        






a=list(dt.items())
b=sorted(a)
i=0
num={}
while i<len(b):
    sum=list(b[i])
    j=0
    while j<len(sum)-1:
        num[sum[j]]=sum[j+1]
        j=j+1
    i=i+1
print(num)




