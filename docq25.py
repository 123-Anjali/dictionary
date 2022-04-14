num=int(input("number items"))
dict={}
for i in range (num):
    a=input("enter string")
    for i in a :
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
print(dict)
