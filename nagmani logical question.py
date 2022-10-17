a={"naga":5,"likki":7,"pavani":8}
for i in a:
    print(repr(a[i]),":",repr(i))




b={"naga":"x","y":{"r":26,"z":36}}
for i in b:
    if type (b[i])==dict:
        for j in b[i]:
            print(j,":",b[i][j],end=" ")