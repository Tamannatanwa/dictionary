# Q21.Write a Python program to print all unique values in a dictionary. 

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)
i=0
x=[]
while i<len(L):
    for j in L[i]:
        if L[i][j] not in x:
            x.append(L[i][j])
    i=i+1
print(set(x))