# a=[1,2,3,5,6]
# a=[3,4,7,8,9]
# i=0
# while i<len(a)-1:
#     num=a[i]-a[i+1]
#     if num==-1:
#         pass
#     else:
#         print(a[i])
#     i=i+1






# def sum(a):
#     i=0
#     while i<len(a)-1:
#         num=a[i]-a[i+1]
#         if num==-1:
#             pass
#         else:
#             print(a[i+1])
#         i=i+1
# a=[1,2,4,5,7,8,9]
# sum(a)





d={"a":[4,6,7],
   "b":[1,2,3],
   "c":[5,11,87]}
for i in range(len(d)):
    sum=0
    pro=1
    sub=0
    for j in d:
        sum+=d[j][i]
        pro*=d[j][i+1]
        sub-=d[j][i+2]
    print(sum)
    print(pro)
    print(sub)
    break







# d={"a":[4,6,7],
#    "b":[1,2,3],
#    "c":[5,11,87]}
# sum=0
# pro=1
# sub=0
# k=0
# for i in d:
#    sum+=d[i][k]
#    pro*=d[i][k+1]
#    sub-=d[i][k+2]
# print(sum)
# print(pro)
# print(sub)