dict=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
a={}
for x,y in dict:
    a.setdefault(x,[]).append(y)
print(a)