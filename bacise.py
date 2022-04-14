# dict1={"name":"Raju","mark":56,"model":"mustang"}
# dict1.pop("model")
# print(dict1)

# dict={"name":"Raju","mark":56,"model":"mustang"}
# dict.clear()
# print(dict)

# my={"name":"Raju","mark":56,"model":"mustang"}
# x=my.copy()
# print(x)

# my={"name":"Raju","mark":56,"model":"mustang"}
# x=my.fromkeys("model")
# print(x)



# my_dict={"name":"Raju","mark":56,"model":"mustang"}
# x=my_dict.get("model")
# print(x)



# my_dict={"name":"Raju","mark":56,"model":"mustang"}
# y=my_dict.items()
# print(y)


# dict={"name":"anjali","model":"mustang","brand":"ford","year":2020}
# dict.popitem()
# print(dict)

# my_dict={"name":"Raju","mark":56,"model":"mustang"}
# x=my_dict.setdefault("name")
# print(x)


# my_dict={"name":"Raju","mark":56,"model":"mustang"}
# my_dict.update({"name":"meena"})
# print(my_dict)





# a = {(1,2):1,(2,3):2}
# print(a[1,2])


# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])



# fruit = {}
# def addone(index):
#     if index in fruit:\
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
#         addone('Apple')
#         addone('Banana')
#         addone('apple')
#         addone('Apple')
# print(len(fruit))
# print(fruit)



# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print(len(Details["Student"])) 




# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)



# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))


# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)



# details={"name":"Shanti","age":12,"email":"shanti@navgurukul.org",}
# print(details["name"])
# print(details["email"])
# print(details["age"])


# dict={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict:
#     sum=sum+i
# print(sum)




# dict={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15}
# for i in dict:
#     dict[i]=i**2
# print(dict)


# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(s)
#     c.update(a)
# print(c)


from telnetlib import X3PAD


b={"a 001":"english","b 002":"hindi"}
d={}
for i in b:
    for x in i:
        k=i.replace(" ","",)
        for i ,x in b.items():
            d.update({k:x})
print(d)


