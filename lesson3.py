# -*- coding: utf8-8 -*-

#lists:
not_a_list = (1,2,)
list1 = [1,2]

long_list = [
    1,
    7,
    3,
    4,

]
list2 = list(not_a_list) # show _bulltin_

#get the tuple back by:"new_tuple = tuple(list2)"

print(list1 == list2, not_a_list ==list1)


#list operations:
# add
# Note the difference between 'append()' and '+-' for tuples
list1.append(3)