"""
1. Игра пятнашки
2. Поле состоит из клеток от 1 до 15 и пустой клетки (x)
3. Управление ведется кнопками "wasd", двигается пустая клетка
4. В начале игры поле перемешено в случайном порядке
5. Пользователь не должен соверашть непозволительные шаги. Например, из-за ограничений рамки поля. Ему должно показываться сообщение о том, 
что он пытается совершить непозволительный ход
6. Пользователю дожно быть видно поле. Оно представляет собой матрицу 4 на 4. Пустую клекту обозначаем как x.
 При каждом действии пользователя поле рисуется еще раз - ниже в консоли
7. Игра заканчивается, когда все клетки стоят по-порядку, а пустая клетка - последняя. 
В конце игры пользователю показывается, сколько ходов он совершил
8. Выход из игры происходит при помощи KeyboardInterrupt. Исключение должно быть обработано. 
Пользователю должна быть выведена фраза "shutting down"

**Дополнительно:
1. Обратите внимание, что не любое поле оставляет возможность закончить игру, необходимо придумать корректный алгоритм генерации взамен простого перемешивания
2. Тесты, которые приложены к работе должны проходить
3. Вам необходимо посмотреть, как работают самописные тесты, которые приложены к работе
"""

# -*- coding: utf-8 -*-

import random

# random.shuffle() - перемешать поле

EMPTY_MARK = 'x'


MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)
    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')
    

def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    pass


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    position_x = field.index(EMPTY_MARK)
# Здесь я обрабатываю ошибки ,в случае если пользователь походит не туда
    if key == 'w' and position_x <= 3:
        raise IndexError('Шаг вверх невозможен')
    elif key == 'a' and position_x :
        raise IndexError('Шаг вправо невозможен')
    elif key == 's' and position_x :
        raise IndexError('Шаг вниз невозможен')
    elif key == 'd' and position_x :
        raise IndexError('Шаг влево невозможен')
    

def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    pass


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    print_field(field)
    while not is_game_finished(field):
        key = handle_user_input()
        try:
            field = perform_move(field, key)
        except IndexError as e:
            print(e)
        print_field(field)
    

if __name__ == '__main__':

    main()