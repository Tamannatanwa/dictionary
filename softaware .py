data=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
i=0
while i<len(data):
    for j in data[i]:
        print(j,":",data[i][j])
    i=i+1

