# d={"a":[4,8,9],"b":[6,7,8],"c":[9,10,11]}
# x={}
# for i in d:
#     sum=0
#     for j in d[i]:
#         sum+=j
#     a=sum/len(d[i])
#     x[i]=a
# print(x)



# d={"anjali":[74,58,79,45,67],
#    "biju":  [46,78,58,77,68],
#    "ceema": [89,56,79,70,71]}
# x=list(d.values())
# y=list(d)
# i=0
# v={}
# while i<len(x):
#     j=0
#     sum=0
#     while j<len(x):
#         sum+=x[j][i]
#         j=j+1
#     ave=sum/len(x)
#     v[y[i]]=ave
#     i=i+1
# print(v)
    
    











d={"anjali":[74,58,79,45,67],
   "biju":  [46,78,58,77,68],
   "ceema": [89,56,79,70,71]}
x=list(d.values())
i=0
v=[]
sub=int(input("enter the sunject..."))
while i<sub:
    j=0
    sum=0
    while j<len(x):
        sum+=x[j][i]
        j=j+1
    ave=sum/len(x)
    v.append(ave)
    i=i+1
print(v)
    