car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.keys()
car["color"] = "white"
y=car.get("year")
print(x,"\n",y)