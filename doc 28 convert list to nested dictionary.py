# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# {1: {2: {3: {4: {}}}}}


list = [1, 2, 3, 4]
i=0
x=dict()
n=x
while i<len(list):
    x[list[i]]={}
    x=x[list[i]]
    i=i+1
print(n)




num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)
    





