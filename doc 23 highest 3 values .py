# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
a={1:4,2:9,3:16,4:35,5:67}
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

