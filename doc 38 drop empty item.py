a={'c1': 'Red', 'c2': 'Green', 'c3': None}
x=dict()
for i in a:
    if a[i]==None:
        pass
    else:
        x[i]=a[i]
print(x)
