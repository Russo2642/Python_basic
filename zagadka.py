import random
n = (random.randint(0,100))
print(n)
print("""Здравствуй дружище
Я вижу ты хочешь сыграть со мной в игру 
Угадай число""")
print("""Эта игра просто произведение искусства
в области консольных игр
не создано учениками MIT, но даже лучше :)""")
print("""Данная игра является улучшенным аналогом висельницы""")
print("начнем?")
print("press start")
press_start = ['start', 'старт']
press_start1 = input()
if press_start1.lower ==  press_start[0] or [1]:
    print('Ну что ж вторая проверка, потому-что играем на деньги')
    moneyamount = float(input("внеси сумму:  "))
    print('Ты прочитал условия, решай (играть или нет)')
    a = input("твое решение?")
    a1 = ['да', 'нет', 'yes', 'no']
    if a.lower() == a1[0] or a1[2]:
        print("""Молодец, начинаем,
        дается только 6 попыток
        при окончании попыток игра прекратится автоматически""")
        print(moneyamount)
        t = 0
        while t < 6:
            enterrednumber = int(input())
            # enterrednumber2 = int(input())
            if enterrednumber == n:
                print("ух какой везунчик, держи выплату в размере 20 \%")
                card_num = input("номер карты:  ")
                t = t + 6 
                moneyamount_win = moneyamount + 0.2 * moneyamount
                print("выполнен платеж на сумму {} на карту {} ".format(moneyamount_win, card_num))

            elif enterrednumber < n :
                print("промах, на кону денежки, меньше нужного числа")
                moneyamount = moneyamount - 0.2 * moneyamount
                print(moneyamount)
                print("вот столько вечнозеленых у тебя осталось")
                print("try again")
                
                t = t + 1

            elif 0 < enterrednumber < int(n * 0.5):
                print('потеплее, но всервно не оно, число меньше половины нужного')
                moneyamount = moneyamount - 0.4 * moneyamount
                print(moneyamount)
                print("вот столько вечнозеленых у тебя осталось")
                print("try again")
                
                t = t + 1
            elif enterrednumber > n:
                print("нет,но ты все ближе,твое число больше загаданного")
                moneyamount = moneyamount - 0.6 * moneyamount
                print(moneyamount)
                print("вот столько вечнозеленых у тебя осталось")
                t = t + 1 
            elif enterrednumber > int(n/2):
                print("ты уже близок к истине, твое число больше половины загаданного")
                moneyamount = moneyamount - 0.8 * moneyamount
                print(moneyamount)
                print("вот столько вечнозеленых у тебя осталось")
                t = t + 1 
            elif 10 > enterrednumber > n :
                print('загаданное число точно точно лежит в пределе десятков')
                moneyamount = moneyamount - 0.85 * moneyamount
                print(moneyamount)
                print("вот столько вечнозеленых у тебя осталось")
                t = t + 1 
            print('exit')


                


















