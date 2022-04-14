my={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a=[]
for i in my:
    a.append(my[i])
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j=j+1
    i=i+1
dict1={}
for k in range (len(a)):
    for i,j in my.items():
        if j==a[k]:
            dict1.update({i:a[k]})
print(dict1)

my={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
a=[]
for i in my:
    a.append(my[i])
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]>a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j=j+1
    i=i+1
dict1={}
for k in range (len(a)):
    for i,j in my.items():
        if j==a[k]:
            dict1.update({i:a[k]})
print(dict1)






# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}

# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}