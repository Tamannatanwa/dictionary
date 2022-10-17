my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
}
x=0
y=0
z=0
for i in my_dict.values():
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