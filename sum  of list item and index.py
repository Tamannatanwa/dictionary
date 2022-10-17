a=[2,1,7,5,3,8]
i=0
v=[]
while i<len(a):
    sum=a[i]+(i+1)
    while sum>0:
        x=sum%10
        sum=sum//10
    v.append(x)
    i=i+1
print(v)