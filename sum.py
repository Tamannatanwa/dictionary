a=int(input("enter the length.."))
i=0
b=[]
sum=0
while i<a:
    x=int(input("enter the number..."))
    b.append(x)
    num=b[i]
    sum+=num
    i=i+1
ave=sum/len(b)
print(sum)
print(ave)