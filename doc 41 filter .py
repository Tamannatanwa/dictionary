#41.Write a Python program to filter the height and width of students, which are stored in a dictionary. 
a={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
x={}
for i in a:
    v=list(a[i])
    j=0
    while j<len(v)-1:
        if v[j]>6 or v[j+1]>70:
            x[i]=v[j],v[j+1]
        j=j+1
print(x)




            
            
            