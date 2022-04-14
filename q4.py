dic={1:"NAVGURUKUL",2:"IN",3:{"a":"WELCOME","B":"TO","C":"DHARMASALA"}}
for i in dic:
    if type(dic[i])==type(dic):
        for j in dic[i]:
            del dic [i][j]
            break
print(dic)