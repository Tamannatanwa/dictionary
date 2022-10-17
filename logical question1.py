a="aaabbcaabb"
i=0
b=[]
while i<len(a)-1:
    if a[i] not in b:
        b.append(a[i])
    i=i+1
b.append(a[i-2])
b.append(a[i])
print(b)



# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)




# a=[1,3,4,5]
# i=-1
# b=[]
# while i>=-len(a):
#     b.append(a[i])
#     i=i-1
# print(b)


