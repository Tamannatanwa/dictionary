a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
x=0
y=0
z=0
for i in a.values():
    if i>x:
        z=y
        y=x
        x=i
    elif i>y:
        z=y
        y=i
    elif i>z:
        z=i
print(x,"is first highest value")
print(y,"is second highest value")
print(z,"is third highest value")

