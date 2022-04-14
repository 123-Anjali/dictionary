# from typing import Counter


# my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# k=[]
# k=Counter(my_dict)
# high=k.most_common(3)
# for i in high:
#     print(i[1])


my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
max1=0
max2=0
max3=0
for i in my_dict:
   for  j in my_dict:
       if my_dict[j]>max1:
           max1=my_dict[j]
       if my_dict[j]>max2  and my_dict[j]!=max1:
            max2=my_dict[j]
       if my_dict[j]>max3 and my_dict[j]!=max1 and my_dict[j]!=max2:
            max3=my_dict[j]
print(max1,max2,max3)
