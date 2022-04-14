


dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100,"f":500}
l=[]
for i in dict:
    l.append(dict[i])
max=0
min=l[0]
i=0
while i<len(l):
    if l[i]>max:
        max=l[i]
    if l[i]<min:
        min=l[i]
    i=i+1
print(max,min)
