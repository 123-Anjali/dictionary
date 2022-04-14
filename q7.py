dic={"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"},{"six":"9"},{"seven":"7"}
c=[]
for i in dic:
    for j in i:
        if i[j] not in c:
           c.append(i[j])
print(c)