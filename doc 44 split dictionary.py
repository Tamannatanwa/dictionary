d= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
list=[]
a,b=d.values()
for i in range(len(a)):
    for j,k in d.items():
            b=({j:k[i]})
            list.append(b)
print(list)
    
    
    