dic={"ball":"red",  "bat":4, "wickets":8, "ball":"green", "bat":3}
# temp = []
# res = dict()
# for key, val in dic.items():
#     if val not in temp:
#       temp.append(val)
#       res[key] = val
# print(res)

a={}
for i in dic:
    if i not in a:
        a[i]=dic[i]
print(a)