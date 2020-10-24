# Циклы for и while

#for i in range(2, 20, 2): # range(m) = range(n, m-1)
    #print(i) 



# range(n, m, y) 
    # параметр n - от какого числа
    # параметр m - до какого числа
    # параметр y - шаг


# a = [1, 2, 3, 4, 5]

# for i in a:
#     print(i)

# тип данных int не итерируемый 


a = int(input('введите число: '))

for i in range(a):
    if i % 2 == 0:
        print(i)