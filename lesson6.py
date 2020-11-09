#1.Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, если оно меньше 0 - TypeError, если оно больше 10 - IndexError. Обрабатываем ошибку, говорим пользователю, в чем его ошибка
# a = int(input("введите число:"))

# try:
#     if a%2==0:
#         raise ValueError
#     if a<0:
#         raise TypeError
#     if a>10:
#         raise IndexError

# except ValueError as b:
#     print(" ввели четное число", b)
# except TypeError as c:
#     print(" число меньше нуля ", c)
# except IndexError as d:
#     print("число больше 10", d)

#2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть. Если все хорошо - пишите объект в консоль. 
# list1 = ["str", "home", "car", "work"]
# print("dlina spiska ot 0 do 4", len(list1))
# user_input = int(input("vvedite index:"))

# try:
#     print("vawe znachnie:" +  list1[user_input])
#     if user_input>len(list1):
#         raise IndexError("bolwe chem spisok")
#     if user_input<0:
#         raise IndexError
# except IndexError as index1:
#     print(" vy vveli nekorektnoe znachenie", index1)

 #Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0   

# def myfunc(a,b):
#     if a or b >0:
#         return a+b
#     if a or b <0:
#         return a-b 
# print(myfunc(2,5))

#Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль

# def newfunc(a,b,c):
#     new_list = []
#     new_list.append(max(a,b,c))
   
    
# print(newfunc(2,11,6))

#аписать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. Если флаг действителен - возвращаем новый список 

# def newnewfunc(spisok, case):
#     lis3 = []
#     if case:
#         for elements in spisok:
#             if elements%2==0:
#                 return lis3.append(elements)
#         for elements in spisok:
#             if elements%2!=0:
#                 return lis3.append(elements)

            
# print(newnewfunc([1,2,3,4,5,6], False))

#Написать функцию, которая принимает любое количество аргументов чисел. Среди них она находит максимальное и минимальное. И возвращает оба

#  def some_function_1(*args):
#      some_list = []
#      some_list.append(max(args))
#      some_list.append(min(args))
#      return some_list
    
    
# print(some_function_1(1,2,3,4,5,6,7))

#.Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему

# def some_function_2(stroka, case=True):
#     if case:
#         return stroka.upper()
#     else:
#         return stroka.lower()

# print(stroka, True)

#Написать функцию, которая принимает любое количество позиционных аргументов - строк и один парматер по-умолчанию glue, который равен ':'.


def some_function_3(*args, glue=":"):
    list55 = []
    for elements_1 in args:
        if len(elements_1)>3:
            list55.append(elements_1)  # glue.join(list55)
    return glue.join(list55)
print(some_function_3("home","house","cat", "dog"))
    
    
