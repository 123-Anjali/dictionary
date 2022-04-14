dict1={"Alex": ["sub1","sub2","sub3"],"David":["sub1","sub2"]}
count=0
for i in dict1:
    j=0
    while j<len(dict1[i]):
        count=count+1
        j=j+1
print(count)
