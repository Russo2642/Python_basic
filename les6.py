a = int(input('Число: '))
try:
    if a%2==0:
        raise ValueError()
    if a<0:
        raise TypeError()
    if a>10:
        raise IndexError()
except ValueError as a:
    print("Четное число недопустимо!")
except TypeError as a:
    print("Число меньше нуля!")
except IndexError as a:
    print("Число больше 10!")


#2
user_list = [1, 3, 5, 7, 9, 11]
user_index = int(input('Please, input index: '))
try:
    print('Item with index {} is {}'.format(user_index, user_list[user_index]))
except IndexError as e:
    print('{}, Your index is out of range'.format(e))

    #1
def my_custom_func(arg1,arg2):
    if arg1 > 0 and arg2 > 0:
        return arg1 + arg2
    if arg1 < 0 and arg2 < 0:
        return arg1 - arg2
    if arg1 != arg2:
        return 0
print(my_custom_func(10,2))
    
    #2
def my_custom_func2(arg1,arg2,arg3):
	my_list = list(locals().values())
	list_of_max = []
 
	while len(list_of_max) < 2:
	    list_of_max.append(max(my_list))
	    my_list.remove(max(my_list))
 
	print('List of two maximums: {}'.format(list_of_max))
 
my_custom_func2(10,2,5)

#3
def my_custom_func3(list_of_numbers,case):
    temp_list = []
    if case:
        for number in list_of_numbers:
            if number % 2 == 0:
                temp_list.append(number)
    else:
        for number in list_of_numbers:
            if number % 2 != 0:
                temp_list.append(number)
    return temp_list

    print(my_custom_func3([1, 2, 3, 4, 5], False))

#1 
#print(my_custom_func4(1,2,3,4,5,6,7,8,9))
#temp2 = []
#temp2.append(max())
#temp2.append(min())
#return temp2

#2
def my_custom_func5(string,case=True):
	if case:
		return string.upper()
	else:
		return string.lower()
 
print(my_custom_func5('test', False))


	
 



    