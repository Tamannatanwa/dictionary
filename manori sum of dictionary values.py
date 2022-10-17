d={"a":[4,8,9],"b":[6,7,8],"c":[9,10,11]}
x={}
for i in d:
    sum=0
    for j in d[i]:
        sum+=j
    x[i]=sum
print(x)