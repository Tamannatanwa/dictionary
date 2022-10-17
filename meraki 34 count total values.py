# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# i=0
# count=0
# for i in dict1.values():
#     x=0
#     while x<len(i):
#         count+=1
#         x=x+1
# print(count)




# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# sum=0
# for i in dict1.values():
#   for item in i:
#     sum+=1
# print(sum)

dict1={"c1":[1,2,3],"c2":[5,6,7],"c3":[9,10,11]}
b=[]
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