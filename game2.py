import random

WordList = ['самолет', 'поезд', 'путешествие', 'виселица']
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

print('В И С Е Л И Ц А')
missedletters=''
correctletters=''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(Viselica, missedletters, correctletters, secretWord)

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
        else: missedletters = missedletters + guess

#Проверка условия проигрыша
if len(missedletters) == len(Viselica)
    displayBoard(Viselica, missedletters, correctletters, secretWord)  
    print('У вас не осталось попыток')

    if gameIsDone:
        if playAgain():
            missedletters = ''
            correctletters = ''
            gameIsDone = False
            secretWord = getRandomWord(WordList)