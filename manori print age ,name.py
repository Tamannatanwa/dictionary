i=1
x={}
while i<=5:
    name=input("enter the name...")
    age=int(input("enter the age.."))
    x[name]=age
    i=i+1
max=0
c={}
for i in x:
    if x[i]>max :
        max=x[i]
print(max)
    
    
