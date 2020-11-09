import random

WORDS = ['самолет', 'поезд', 'путешествие'].split(".")
#случайный выбор слов 
input(int("Ugadaite slovo. U vas est' 12 popytok! Pristupim?: "))
if start == 'da':
    print('Pognali!')
else: 
    #start == 'no':
    print('exit')

def step():
    print('Vvedite bukvu: ')
    letter=input()
while letter not in "абвгдежзийклмнопрстуфхцчшщьыъэюя":
    letter = input('Vvedite bukvu ')
if letter in chosing():
    for i in range(len(chosing)):
        if chosing()[i]==letter:
            intro()[i]=letter
    print(intro())
elif letter not in chosing():
    print('Ne ugadali')
chosing()
intro()
step()
    