x={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
y=x["Cierra Vega"]
count=0
a=list(x.values())
i=0
while i<len(a):
    if a[i]==y:
        count+=1
    i=i+1
if len(x.values())==count:
    print(True)
else:
    print(False)
    
    
    
    
    
    
    
    
    
    
