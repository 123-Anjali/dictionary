dic={1:10,1:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
b={}
i=0
while i <len(dic):
    b.update(dic)
    b.update(dic2)
    b.update(dic3)
    i=i+1
print(b)