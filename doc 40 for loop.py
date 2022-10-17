list1= ["S001", "S002", "S003", "S004"] 
list2= ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
list3= [85, 98, 89, 92]
result=[{x:{y:z}} for x,y,z in zip(list1,list2,list3)]
print(result)