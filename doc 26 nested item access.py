dict1={"c1":[1,2,3],"c2":[5,6,7],"c3":[9,10,11]}
b=[]
for j in dict1.keys():
    print(j,end=" ")
print()
for i in dict1.values():
  b.append(i)
i=0
while i<len(b):
  j=0
  while j<len(b[i]):
    print(b[j][i],end=" ")
    j=j+1
  print()
  i=i+1