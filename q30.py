b={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d={}
for i in b:
    for x in i:
        k=i.replace(" ","",)
        for i ,x in b.items():
            d.update({k:x})
print(d)




