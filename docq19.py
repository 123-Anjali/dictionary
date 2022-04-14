student_data={'id1':{'name':['Sara'],'class':['v'],'subject_integration':['english,math,science']},
'id2':{'name':['David'],'class':["v"],"subject_integration":["english,math,science"]},
"id3":{"name":["Sara"],"class":["v"],"subject_integration":["english,math,science"]},
"id4":{"name":["Surya"],"class":["v"],"subject_integration":["english,math,science"]},}
b={}
for i in student_data:
    for  j in student_data[i]  :
        if j in student_data[i]:
            b.update([j])
print(b)



# {'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 'id4': {'subje
# ct_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']}, 'id1': {'subject_integration'
# : ['english, math, science'], 'class': ['V'], 'name': ['Sara']}} 

