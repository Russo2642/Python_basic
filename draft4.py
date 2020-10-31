list1 = [5,3,6,1,4,2]
list1.sort()  
print(list1)

dict1 = {1:"odin", 2:"dva", 3:"tri"}
for key,value in dict1.items():
    print(key,value)

tuple1 = (1.5,6.3,9.2)
print(max(tuple1), min(tuple1))

name1,name2,name3 = ["Earth","Russia","Moscow"]
print(name1 + "->" + name2 + "->" + name3)

list2 = '/bin:/usr/bin:/usr/local/bin'
list_2 = list2.split(":")
print(list_2)

a = range(0,101)
for element in a:
    if element%7==0:
        print("\nделится на 7 без остатка:", element, end="")
for element_1 in a:
    if element_1%7!=0:
        print("\nделится на 7 c остатком:", element_1, end="")

list3 = [1,"str", "home"]
print(list3.index(1))
print(list3.index("str"))
print(list3.index("home"))

list4 = ["to delete", " to sleep", "to study"]
del list4[0]
print(list4)

list5 = [1,6,2,6,9,3,5,4,7,8]
list5.sort(reverse=True)
print(list5)
   
