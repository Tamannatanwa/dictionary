a={1:{'course':"python","fees":15000},
   2:{"course":"javascript","fees":10000}}
c={}
print("keys:")
for id in a:
    for k in a[id]:
        print(k,"=",a[id][k])
        c[k]=a[id][k]
        print(k)
        print(a[id][k])
print(c)
print()
