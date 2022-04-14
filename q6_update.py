# my={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# my.update({"ball":"red","bat":4})
# print(my)



my={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
my.update({"ball":"red","bat":4})
d={}
for i in my:
    d.update(my)
print(my)

