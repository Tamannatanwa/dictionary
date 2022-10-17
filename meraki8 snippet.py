


a={1:"A",2:"B",3:"C"}
print(a.get(5,4))



a={1:"A",2:"B",3:"C"}
print(a.get(1,4))



person= {'1': 'RAM', '2': 17,}
person[3] = 'male'
print(person)



details={
    'Name': 'RAM',
    'Age': 17, 
    'student':{
        'id': 22,
        'place': 'dharamsala'
        }
} 
details['student']['id']=35
print(details)



classes ={
    "room1":  "6th",
    "room2":  "7th",
    "room3":  "8th"
    }
# mydict=classes.copy()
mydict=classes
print(mydict)
print(classes)