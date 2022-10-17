# Ax={'a':2,'b':'A','c':'d'}
# c=Ax.keys()
# print(c)


# x=int(input("enter the number.."))
# y=int(input("enter the number..."))
# i=1
# sum=0
# while i<=x:
#     sum+=y
#     i=i+1
# print(sum)



# for i in a:
#     sum+=a[i]
# print(sum)








# x=int(input("enter the number.."))
# y=int(input("enter the number..."))
# sum=0
# while x<=y:
#     sum+=y
#     x=x+1
# print(sum)








# dict1={"node":{"nam":"emily","year":2004},"node2":{"name":"john","year":2023},"node3":{"ravi":"email","year":2014}}



# a=["cofee","techm","iti","wipro","mindtree","tcs","infy","hcltech"]
# b=a[::-1]
# # i=-1
# # b=[]
# # while i>=-len(a):
# #     b.append(a[i])
# #     i=i-1
# print(b)



# a=[print(i) for i in range(20,51)]



# s=[12,34,4,23,[44,45,12,90,["ff","sa",67,99,3]],{"a":1,"b":2,"c":3,"d":4},[77,32,11]]
# c=s[4][4][1]
# print(c)







a={"a":{2:"r",3:{2,3}},"b":{3:"t",4:{4,5}},"c":{2:"k",5:{6,7}},"d":{3:"s",6:{7,8}}}
b=[]
for i in a:
    c=[]
    for j in a[i]:
        if type (a[i])==dict:
            for k in a[i][j]:
                c.append(k)
    b.append(c)
print(b)
    
