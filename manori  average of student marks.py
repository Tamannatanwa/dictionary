d={"anjali":[74,58,79,45,67],
   "biju":  [46,78,58,77,68],
   "ceema": [89,56,79,70,71]}
x=[]
n=int(input("enter the subject.."))
for i in range(n):
    sum=0
    for j in d:
        n=d[j][i]
        sum+=n
    ave=sum/len(d)
    x.append(ave)
print(x)