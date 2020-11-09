# Игра. Виселица

# Решаем эту задачу с помощью функций 

"""
1. Попыток 10
2. Создать 5 слов. Рандомно вывести одно слово пользователю (количество нижних подчеркиваний)
3. В конце вывести слово - если юзер угадал и если не угадал 
4. Создадите функцию is_game_finished() - которая отвечает за окончание игры.
5. Функция main() - отвечает за логику игры
"""

import random

WORDS = ['Python', 'машина', 'строка']
# random.choice(WORDS)

computer = random.choice(WORDS)
# a = random.choice(WORDS)
# zdes risuem probely

def write_space():
    word = []
    if len(computer)>0:
        word.append(computer)
        return word.insert[0,"_"]
    write_space()

# tut vvdodim bukvy i menyaem mestami s probelom

def write_word():
    user_input = input("write some word:")
    for element in write_space:
        if user_input == computer:

# tut otvechaem za kolichestvo popytok
           
def user_try():
    try_1 = 0
    while user_input<12:
        try_1+=1
        if user_input!=computer:
            print("no such letters")
        if user_input==computer:
    user_input()


