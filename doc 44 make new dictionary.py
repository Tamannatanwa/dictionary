def list(marks):
    keys = marks.keys()
    vals = zip(*[marks[k] for k in keys])
    result = [dict(zip(keys, v)) for v in vals]
    return result
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(list(marks))
    