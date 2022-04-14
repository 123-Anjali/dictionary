dict={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
num=int(input("enter the number"))
l=[]
for i in dict:
    l.append(dict[i])
print(num in l)
