b=[3,7,4,2,8,6,21,1]
i=0
max=0 
smax=0
tmax=0
fmax=0
min=b[i]
smin=b[i]
tmin=b[i]
fmin=b[i]
x=[]
while i<len(b):
    if b[i]>max:
       fmax=tmax
       tmax=smax
       smax=max
       max=b[i]
    elif b[i]>smax:
        fmax=tmax
        tmax=smax
        smax=b[i]
    elif b[i]>tmax:
        fmax=tmax
        tmax=b[i]
    elif b[i]>fmax:
        fmax=b[i]
    if b[i]<min:
        fmin=tmin
        tmin=smin
        smin=min
        min=b[i]
    elif b[i]<smin:
        fmin=tmin
        tmin=smin
        smin=b[i]
    elif b[i]<tmin:
        fmin=tmin
        tmin=b[i]
    elif b[i]<fmin:
        fmin=b[i]
    i=i+1
print(fmax,fmin,tmin)
n=max+min
m=smax+smin
k=tmax+tmin
h=fmax+fmin
x.append(n)
x.append(m)
x.append(k)
x.append(h)
print(x)
j=-1
n=[]
while j>=-len(x):
    num=str(x[j])
    c=num[-1]
    n.append(c)
    j=j-1
print(n)
    