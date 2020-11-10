import random

WordList = ['viselica', 'samolet', 'more', 'kacheli']
#случайный выбор слов 
start = input("Ugadaite slovo. U vas est' 12 popytok! Pristupim?: ")
if start == 'da':
    print('Pognali!')
else: 
    start == 'no'
    print('exit')

def getRandomWord(WordList):
    wordIndex = random.randint(0, len(WordList) - 1)
    return WordList[wordIndex] #эта функция возвращает случайное слово, которое выбирает из заранее созданного списка

def displayBoard(Viselica, missedletters, correctletters, secretWord):
    print(Viselica[len(missedletters)])
    print()

    print('Неправильные буквы: ', end=' ')
    for letter in missedletters:
        print(letter, end=' ')
    print()

    blanks = '*'*len(secretWord) #Заменяем звездочки на правильно угаданные буквы
    for i in range(len(secretWord)):
        if secretWord[i] in correctletters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    #Показываем загаданное слово с пробелами между букв
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #Возвращает букву, которую ввел игрок. Эта функция проверяет что введена буква, а не какой-то другой символ
    while True:
        print('Введите букву: ')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
        print('Ваша буква: ')
    elif guess in alreadyGuessed:
        print('Вы уже пробовали эту букву, выберите другую')
    elif guess not in 'аоеуисмтпздтшвлц':
        print('Пожалуйста используйте для ввода только кириллицу')
    else:
        return guess

def playAgain():
    #Эта функция возвращает true если игрок решит сыграть еще раз. в противном случае false
    print('Хотите попробовать еще раз? ("DA"или "NET")')
    return input().lower().startswith('DA')

print()
missedletters=' '
correctletters=' '
secretWord = getRandomWord(WordList)
gameIsDone = False

while True:
    displayBoard(missedletters, correctletters, secretWord)

#Вычисляем количество букв которые ввел игрок
guess = getGuess(missedletters+correctletters)

if guess in secretWord:
    correctletters = correctletters + guess

#Проверка условия победы 
foundAllletters = True
for i in range(len(secretWord)):
        if secretWord[i] not in correctletters:
            foundAllletters = False
            break
        if foundAllletters:
            print('Превосходно! Вы отгадали загаданное слово!')

        gameIsDone = True
else:
    missedletters = missedletters + guess

#Проверка условия проигрыша
if len(missedletters) == len(Viselica):
    displayBoard(Viselica, missedletters, correctletters, secretWord)  
    print('У вас не осталось попыток')

    if gameIsDone:
        if playAgain():
            missedletters = ''
            correctletters = ''
            gameIsDone = False
            secretWord = getRandomWord(WordList)

#333
attempts = 12
WORD = ['АПЕЛЬСИН', 'МАНДАРИН', 'ЯБЛОКО', 'АНАНАС', 'ВИШНЯ'].strip(' ').lower()
Splitted_word = list(WORD)
count_of_chars = len(Splitted_word)
guessed = ['_' for i in range(count_of_chars)]

while True:
    print(' '.join(guessed))
    print('Attempts: ', attempts)
    char = input('Enter letter: ').strip(' ').lower()
    if char in splitted_word:
        for i, c in enumerate(Splitted_word):
            if c == char:
                guessed[i] = char
    else:
        attempts -= 1
    if attempts == 0:
        print('Vy proigrali')
        break

print(' '.join(guessed))
