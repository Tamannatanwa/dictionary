# b=[6,9]
# i=min(b)
# n=max(b)
# c=[]
# while i<=n:
#     # if i==min(b):
#     #     c.append(i)
#     # elif i==max(b):
#     #     c.append(i)
#     c.append(i)
#     i=i+1
# print(c)


x=int(input("enter the length..."))
a=[]
i=0
count=0
z=[]
while i<x:
    c=int(input("enter the number.."))
    a.append(c)
    if a[i] not in z:
        z.append(a[i])
    else:
        count+=1
    i=i+1
print(z)
print(count)