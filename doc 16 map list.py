a=["tamanna","radhika","archana","priyanka","anjali"]
b=[18,21,19,20,22]
z=dict(zip(a,b))
print(z)




a=["tamanna","radhika","archana","priyanka","anjali"]
b=[18,21,19,20,22]
z=dict(map(lambda n ,m:(n,m),a,b))
print(z)