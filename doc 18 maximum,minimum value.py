a={1:2,2:4,3:9,4:16,5:25}
max=0
min=10
for i in a.values():
    if i>max:
        max=i
    if i<min:
        min=i
print(max)
print(min)




