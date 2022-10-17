# list=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# c={x:{y:z} for x,y,z in list}
# print(c)





list=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
i=0
x={}
while i<len(list):
    j=0
    b=[]
    while j<len(list[i])-1:
        b.append(list[i][j+1])
        j=j+1
    x[list[i][0]]=b
    i=i+1
print(x)
    
        
