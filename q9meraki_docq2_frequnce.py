# dict={"M":1,"I":1,"S":1,"S":2,"I":2,"S":3,"S":4,"I":3,"P":1,"P":2,"I":4}
# for i in dict:
#     d=dict
# print(d)
    


dict="w3resource" 
d={}  
for i in dict:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
