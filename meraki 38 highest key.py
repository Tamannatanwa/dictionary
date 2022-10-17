


my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
}
x=" "
y=" "
z=" "
for i in my_dict.keys():
    if i>x:
        z=y
        y=x
        x=i
    elif i>y:
        z=y
        y=i
    elif i>z:
        z=i
print([x,y,z])
    
   
   
    
    
my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
}
x=list(my_dict.keys())
d=dict()
x.sort(reverse=True)
x=x[:3]
print(x)