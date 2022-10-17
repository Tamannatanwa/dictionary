# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}



c=dict()
for i in "w3resource":
    x="w3resource".count(i)
    c[i]=x
print(c)



c=dict()
x="w3resource"
i=0
while i<len(x):
    v=x.count(x[i])
    c[x[i]]=v
    i=i+1
print(c)  



