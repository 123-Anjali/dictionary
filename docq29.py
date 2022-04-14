dict={"name":"zara","school":"c.m.s","claas":"ten"}
l=[]
for i in dict:
    l.append(dict[i])
for i in range (len(l)):
    for j in range(len(l)):
        if l[j]>l[i]:
            c=l[i]
            l[i]=l[j]
            l[j]=c
d={}
for k in range(len(l)):
    for x,j in dict.items():
        if j==l[k]:
            d.update({x:l[k]})
print(d)
