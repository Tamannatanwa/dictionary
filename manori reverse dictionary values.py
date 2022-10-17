d={"a":[4,8,9],"b":[6,7,8],"c":[9,10,11]}
x=dict()
for i in d:
    x[i]=d[i][::-1]
print(x)