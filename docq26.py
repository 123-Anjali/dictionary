my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
list=[]
for i,j in my_dict.items():
    print(i,end=" ")
    list.append(j)
print()
for i in range(0,len(list)):
    for j in range(0,len(list)):
        print(list[j][i],end=" ")
    print()





# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11

