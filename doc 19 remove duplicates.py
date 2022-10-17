# Write a Python program to remove duplicates from Dictionary.
# Sample output:

# {'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 'id4': {'subje
# ct_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']}, 'id1': {'subject_integration'
# : ['english, math, science'], 'class': ['V'], 'name': ['Sara']}} 




x= {'id1': {'name': ['Sara'],
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4':  {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

# result = {}

# for key,value in x.items():
#     if value not in result.values():
#         result[key] = value

# print(result)



new_dict = {}
for i,j in x.items():
    if j not in new_dict.values():
        new_dict.update({i:j})
print(new_dict)


