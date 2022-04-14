dict1={"a":100,"b":200,"c":300}
dict2={"a":300,"b":200,"d":400}
for i in dict2:
    if i in dict1:
        dict1[i]+=dict2[i]
    else:
        dict1[i]=dict2[i]
print(dict1)

   

