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
zamena = "_"

# # zdes risuem probely

# def write_space():
    
    # for elements, item in enumerate(computer):
    #     computer[elements] = zamena
          
    # return computer
        

# # tut vvdodim bukvy i menyaem mestami s probelom

# def write_word():
#     user_input = input("write some letter:")
#     if user_input in enumerate(computer):   # in wordd
#            user_input,zamena = zamena,user_input   #????
#     return computer
        
        
        

# # tut otvechaem za kolichestvo popytok
           
# def user_try(user_input):
#     try_1 = 0
#     while user_input<12:
#         try_1+=1
#         if user_input not in enumerate(computer):
#             print("no such letters")


# logika igry
        

def return_random_word():
    return random.choice(WORDS) 

def hangle_user_input():
    letter = input("write some letter:")
    return letter

def get_initial_statuses(word):
    for elements, item in enumerate(computer):
        computer[elements] = zamena
          
    return computer

def is_game_finished(statuses, current_errors,letter):
    try_1 = 0
    while letter<12:
        try_1+=1
        

def person_check_action(word,statuses,letter):
    if letter not in word:
        return False
    for computer, l in enumerate(word):
        if letter ==l:
            statuses[computer] = True
        return True

def print_word(word,statuses):


def main():
    
    word = return_random_word()
    statuses = get_initial_statuses(word)
    while not is_game_finished():
        letter = hangle_user_input



