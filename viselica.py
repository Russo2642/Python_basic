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

WORDS = ['python', 'glo', 'iqos']
# random.choice(WORDS)

word = random.choice(WORDS)
zamena = "_"

        

def return_random_word():
    return random.choice(WORDS) 

def hangle_user_input():
    letter = input("write some letter:")
    return letter

def get_initial_statuses(word):
    for elements, item in enumerate(word):
        word[elements] = zamena
          
    return word

def is_game_finished(statuses, current_errors,letter):
    current_errors = 0
    while current_errors<12:
        current_errors+=1

    return statuses
        

def person_check_action(word,statuses,letter):
    if letter not in word:
        return False
    for statuses, l in enumerate(word):
        if letter ==l:
            statuses[word] = True
        return True

def print_word(word,statuses):
    
 

def main():
    
    word = return_random_word()
    statuses = get_initial_statuses(word)
    while not is_game_finished():
        letter = hangle_user_input
        print_word(word,statuses)

if __name__ == '__main__':

    main()
        
        
        



