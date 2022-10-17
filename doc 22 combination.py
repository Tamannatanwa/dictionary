# d={'1':['a','b'], '2':['c','d']}
# val1,val2=d.values()
# for i in val1:
#     for j in val2:
#         print(i+j)
        
        



a={'1':['a','b'], '2':['c','d']}
c=[]
for i in a.values():
    c.append(i)
i=0
r=0
while i<len(c):
    j=0
    while j<len(c[i]):
        num=c[r][i]+c[r+1][j]
        j=j+1
        print(num)
    i=i+1
    
    
    
