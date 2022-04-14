from random import randrange


# dic=[{"name":"sakshi","age":17},{"name":"kallu","age":18},{"name":"anjali","age":25},{"name":"vaishali","age":22}]
# l=[]
# for i in range(len(dic)):
#     for x, y in dic[i].items():
#         if x=="age":
#             l.append(y)
# print(l)



# a=str(input("enter the name"))
# i=0
# d={}
# while i<len(a):
#     d.update({a[i]:i})
#     i=i+1
# print(d)






# num=int(input("enter the number"))
# l=[]
# l1=[]
# for i in range(1,num):
#     count=0
#     for j in range (1,num):
#         if i%j==0:
#             count+=1
#     if count==2:
#         l.append(i)
#     else:
#         l1.append(i)
# d={}
# k=0
# while k<len(l):
#     d.update({l[k]:l1[k]})
#     k+=1
# print(d)






    
# dict={1:1,2:4,3:6,4:8,5:10,6:12}
# count=0
# for i in dict:
#     count=count+dict[i]
# print(count)




# b={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# d={}
# for i in b:
#     for x in i:
#         k=i.replace(" ","",)
#         for i ,x in b.items():
#             d.update({k:x})
# print(d)




# id=[1,2,3,4,5]
# a=["a","b","c","d","e","f"]
# b=[12,23,4,6,7]
# d={}
# for i in range(len(id)):
#     d1={}
#     for j in range(len(a)):
#         if i==j:
#             d1.update({a[j]:b[j]})
#     d.update({id[i]:d1})
# print(d)


# num=int(input("enter the number"))
# i=1
# l=[]
# while i<=(num):
#     l.append(i)
#     i=i+1
# print(l)
# d={}
# i=0
# while i<len(l):
#     if l[i]%2==0:
#         d.update({l[i]:"true"})
#     else:
#         d.update({l[i]:"false"})
#     i=i+1
# print(d)


# list=[1, 2, 3, 4]
# new_d=dict={}
# for i in list:
#     dict[i]={}
#     dict=dict[i]
# print(new_d)


# a={'1':['a','b'], '2':['c','d']}
# b=list(a.values())
# for i in b[0]:
#     for j in b[1]:
#         print(i+j)


# roman_dict={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'XD',500:'D',900:'CM',1000:'M'}
# num_list=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
# num=int(input("enter the number"))
# for i in num_list:
#     quo=num//i
#     if quo!=0:
#         for j in range  (quo):
#             print(roman_dict[i],end=" ") 
#     num%=i


a=[1,2,3,4,5]
b=["name","age","class","roll number"]
c=[["arav",14,"9th",32],["amit",12,"7th",7],["anjali",16,"10th",34],["vaishali",18,"12",56]]
dict={}
i=0
while i<len(c):
    j=0
    dic={}
    while j<len(c[i]):
        dic[(b[j])]=c[i][j]
        j=j+1
    dict[(a[i])]=dic
    i=i+1
print(dict)

    
