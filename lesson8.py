# pervaya zadacha

my_friends = {'dias':"taldykorgan", "shalkar":"aktau", "suleimen":"almaty"}

for key in my_friends:
    print(key, "on iz goroda" , my_friends[key])

# vtoraya zadacha

friends_dict = {'Dima': ['song1', 'song2'], 'Sonya': ['song3', 'song4']}


print('sonyas songs are "{}"'.format(friends_dict["Sonya"]))
print(" , ".join(friends_dict["Sonya"]))
# print(len(set(friends_dict['Dima']))



#zadacha 3

friends_name = ["dias","shalkar",'suleimen']
friends_cities = ["taldykorgan", "aktau","almaty"]

anfisa = {}

for i in range(len(friends_name)):
    anfisa[friends_name[i]]=friends_cities[i]

print("Dias iz goroda", anfisa["dias"])



