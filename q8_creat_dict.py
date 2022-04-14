# a={}
from stringprep import c6_set


# num=int(input("number the  elements"))
# a={}
# for i in range (num):
#     k=input("enter the key")
#     v=input("enter the value")
#     a.update({v:k})
# print(a)



data={"name":"anjali","age":20,"brand":"ford"}
a=[]
for i in data:
    a.append(i)
b=[]
for i in data.values():
    b.append(i)
d={}
i=0
while i<len(a):
    c={b[i]:a[i]}
    d.update(c)
    i=i+1
print(d)
