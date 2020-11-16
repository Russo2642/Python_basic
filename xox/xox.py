import random


EQ_X = "X"
EQ_O = "O"
EMPTY = " "
COUNT = 9


def add_board():
    """
    Создание игральной доски
    :return: доска для игры
    """


def write_board(board):
    """
    Отрисовка игральной доски
    :param board: доска
    :return: None
    """
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def pieces():
    """
    Определяет, кто будет играть крестиками, кто - ноликами
    :return: значения крестика и нолика
    """
    


def human_step(board):
    """
    Получение хода человека
    :param board: доска
    :return: поле
    """
    


def computer_step(board, computer, human):
    """
    Получение хода компьютера
    :param board: доска
    :return: поле
    """
    


def winner(board):
    """
    Определение победителя
    :param board: доска
    :return: победитель
    """
    WAYS_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
    


def legal_moves(board):
    """
    Создает список доступных ходов
    :param board: доска
    :return: список ходов
    """
    


def next_turn(turn):
    """
    Переход хода
    :param turn: значение хода
    :return:
    """
    

def main():
    """
    Основной алгоритм запуска игры
    :return: None
    """
    print("""Игра крестики-нолики, противостояние с компьютером\n
    Чтобы сделать ход, необходимо ввести число от 0 до 8. Число однозначно соответствует
    полям доски, как показано на рисунке ниже:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    """)
    


if __name__ == '__main__':
    main()
    input("Нажмите Enter, чтобы выйти")