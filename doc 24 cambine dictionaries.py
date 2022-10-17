data=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d={}
for i in data:
    if i['item'] not in d:
        d[i['item']]=i["amount"]
    else:
        d[i['item']]+=i["amount"]
print(d)

