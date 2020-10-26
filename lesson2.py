# print('Hi,thank you for choosing us, your Arduino Atmega store')
# a = input('enter your name: ')
# b = input('enter your telephone number')
# c = input('enter your ID number')
# print('Welcome {}, I think you will be our loyal customer, your telephone number is {} and ID'.format(a,b,c))
# print('check all information')
# a1 = input(":")
# if "yes" == a1:
#     print('good')
# elif "not" == a1:
    # print('try again')

# #"""Программа выводить в консоль текст загадки и ждать ввода пользователя
# Программа после ввода пользователя ответа должна вывести в консоль результат: правильный ли ответ дал пользователь
# Загадок должно быть 10, тематика вопросов должна быть по первому занятию
# Дополнительные требования (со звездочкой или сложные, необязательно для выполнения):
# Программа должна в конце игры сказать, сколько ответов дал пользователь: сколько из них было верных
# Программа должна не учитывать регистр ответа: "Python"



print('hi bro, now we will solve problems about Python')
print("1) when was python invented?")
print('1955,1945,1989,1991')
a = input('answer:')
r = 0
if a == '1991':
    print('excellent')
    r = r + 1
 
elif a == '1989':
    print('bad')
    r = r
  
elif a == '1955':
    print('bad')
    r = r
  
elif a == '1945':
    print('bad')
    r = r





print('2) right or not that 123 is string')
print('yes, not , don,t know')
b = input('answer:')
if b.lower() == 'yes':
    print('bad')
    r = r
elif b.lower() == 'not':
    print('excellent')
    r = r + 1
 
elif b.lower() == 'don,t know':
    print('bad')
    r = r
   

print('total: ')
print(r)

if r == 2:
    print('great!!!')
elif r == 1:
    print('not bad bro')
elif r == 0:
    print('you are stupid')



    