from stringprep import c7_set


my={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max=0
max2=0
max3=0
max4=0
max5=0
l=[]
for i in my:
    for j in my:
        if my[j]>max:
            max=my[j]
            m=j
        if my[j]>max2 and my[j]!=max:
            max2=my[j]
            c=j
        if my[j]>max3 and my[j]!=max2 and my[j]!=max:
            max3=my[j]
            d=j
        if my[j]>max4 and my[j]!=max3 and my[j]!=max2 and my[j]!=max:
            max4=my[j]
            k=j
        if my[j]>max5 and my[j]!=max4 and my[j]!=max3 and my[j]!=max2 and my[j]!=max:
            max5=my[j]
            n=j
l.append(m)
l.append(c)
l.append(d)
l.append(k)
l.append(n)
print(l)