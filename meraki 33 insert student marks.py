# Take input of name and marks of 10 students and store to a dictionary.
a=int(input("enter the length.."))
b={}
i=0
while i<a:
    x=input("enter the element..")
    y=int(input("enter the marks.."))
    b[x]=y
    i=i+1
print(b)






details={}
for i in range(5):
   n=input("enter name:")
   m=input("enter marks:")
   details[n]=m
print(details)
