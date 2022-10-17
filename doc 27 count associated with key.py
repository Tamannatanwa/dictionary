student = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]
d={}
count=0
for i in student:
    if "id" in i:
        count+=2
print(count)














