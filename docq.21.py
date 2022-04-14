data= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
b=[]
for i in range(len(data)):
    for j,x in data[i].items():
        if x not in b:
            b.append(x)

print(b)