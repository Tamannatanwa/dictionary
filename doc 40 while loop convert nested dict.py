list1= ["S001", "S002", "S003", "S004"] 
list2= ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
list3= [85, 98, 89, 92]
y={}
i=0
while i<len(list1):
     j=0
     x={}
     while j<1:
          x[list2[i]]=list3[i]
          j=j+1
     y[list1[i]]=x
     i=i+1
print(y)
     
