# a={'a':100,'b':200,'c':300}
# b={'a':300,'b':200,'d':400}
# d={}
# for i in a: 
#     if i=='a':
#         c=(a.get(i)+b.get(i))
#         d[i]=c
#     elif i=='b':
#         c=(a.get(i)+b.get(i))
#         d[i]=c
#     elif i=='c':
#         c=a.get(i)
#         d[i]=c
# print(d)




# a={'a':100,'b':200,'c':300}
# b={'a':300,'b':200,'d':400}
# d={}
# for x in a:
#     for i in b: 
#         if i in x:
#             d[x]=a[x]+b[i]
    
# d[x]=a[x]
# d[i]=b[i]
# print(d)









a={'a':100,'b':200,'c':300}
b={'a':300,'b':200,'d':400}
d={}
for i in a: 
    if i in b:
        c=(a.get(i)+b.get(i))
        d[i]=c
    elif i not in b:
        c=a.get(i)
        d[i]=c
    for i in b:
        if i in a:
             c=(a.get(i)+b.get(i))
             d[i]=c
        d[i]=b.get(i)
            
print(d)


