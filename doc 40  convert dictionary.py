list = ['S001', 'S002', 'S003', 'S004']
list1=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list2=[85, 98, 89, 92]
x=dict()
i=0
while i<len(list):
    v=dict()
    j=0
    while j<1:
        v[list1[i]]=list2[i]
        j=j+1
    x[list[i]]=v
    i=i+1
print([x])




