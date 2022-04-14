dict={"data1": 100,"data2":-54,"data3": 247}
sum=0
for i in dict:
    sum+=dict[i]
print(sum)


a={"a":{"b":40},"u":{"c":50},"j":{"d":30},"m":{"f":4},"k":{"e":10}}
sum=0
for i in a:
    if type(a[i])==dict:
        for j in a[i]:
            sum=sum+a[i][j]
    else:
        sum=sum+a[i]
print(sum)