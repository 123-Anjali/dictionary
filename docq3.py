n=int(input("enter the elements"))
d={}
for i in range(1,n+1):
    n=i**2
    d.update({i:n})
print(d)

