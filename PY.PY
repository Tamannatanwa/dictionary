a={"a":[1,2,3],"b":[5,4,6],"c":[9,6]}
R=[]
for i in a:
    sum=0
    for j in a[i]:
        sum+=j
    R.append(sum)
print(R)





# a="pythonlanguage"
# x={}
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         c=a.count(a[i])
#         x[a[i]]=c
#     i=i+1
# print(x)



a="pythonlanguage"
x={}
b=[]
for i in a:
    if i not in b:
        b.append(i)
        c=a.count(i)
        x[i]=c
print(x)