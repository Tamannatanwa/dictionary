# Q15.Write a Python program to remove a key from a dictionary.

a={"aniket":19,"priya":16,"tamanna":18,"amrita":15}
b=a.popitem()
b=a.pop("tamanna")
del a["aniket"]
print(a)