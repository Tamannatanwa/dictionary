dictionary={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
c=dict()
for i in dictionary:
    b=""
    for j in i:
        if j==" ":
            pass
        else:
            b+=j
    c[b]=dictionary[i]
print(c)
    
        
    