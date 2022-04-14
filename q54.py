dict={1: ['anjali singh'], 2: ['vaishali singh'], 3: ['sakshi gangwaar'], 4: ['meena mishra'], 5: ['akshat singh']}
l=[]
for i in dict:
    l.append(dict[i])

b=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        b.append(l[i][j])
        
d={}
count=0
for x in range(len(b)):
    count+=1
    for j in range(len(b[x])):
        d.update({count:b[x]})
print([d])





