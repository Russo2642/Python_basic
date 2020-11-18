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
    board = []
    for i in range(9):
        board.append(EMPTY) 
    return board


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
    who_will_who = input("kem hochew byt?:").lower()
    if who_will_who == "x":
        human = EQ_X
        computer = EQ_O
        
    if who_will_who == "o":
        human = EQ_O
        computer = EQ_X
    
    return human,computer
    

        


def human_step(board):
    """
    Получение хода человека
    :param board: доска
    :return: поле
    """
    step = None
    moves = legal_moves(board)
    while step not in moves:
        step = int(input("hod:"))
    return board

    # human = int(input("vvedite chislo ot 0 do 9:"))
    # moves = legal_moves(board)
    # if human not in moves:
    #     moves.append(human)
    # return board


def computer_step(board):
    """
    Получение хода компьютера
    :param board: доска
    :return: поле
    """
   
    step2 = None
    moves = legal_moves(board)
    while step2 not in moves:
        step2 = int(input("hod:"))
    return board

    # computer = int(input("vvedite chislo ot 0 do 9:"))
    # moves = legal_moves(board)
    # if computer not in moves:
    #     moves.append(computer)
    # return board


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
    step = human_step(board)
    step2 = computer_step(board)
    # if human == WAYS_WIN:
    #     return "congratulations"
    # if computer == WAYS_WIN:
    #     return "sorry, computer won"


def legal_moves(board):
    """
    Создает список доступных ходов
    :param board: доска
    :return: список ходов
    """
    new_var = []

    for i in range(COUNT):
        if board[i] == EMPTY:
            new_var.append(i)
    
    return new_var


def next_turn(turn):
    """
    Переход хода
    :param turn: значение хода
    :return:
    """
    if turn == EQ_X:
        return EQ_O
    else:
        return EQ_X

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
    human, computer = pieces()
    turn = EQ_X
    board = add_board()
    write_board(board)
    while not winner(board):
        if turn == human:
            step = human_step(board)
            board[step] = human
        else:
            step2 = computer_step(board)
            board[step2] = computer
        write_board(board)
        turn = next_turn(turn)
        theWinner = winner(board)
    if theWinner == computer:
        print("Computer won")
    else:
        print("You won")
    

if __name__ == '__main__':
    main()
    input("Нажмите Enter, чтобы выйти") 