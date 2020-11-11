import random

start_game = input("do you want to play? Yes or No:").lower()
if "Yes":
    print("lets start")
else:
    exit()

word = ['python',"java", "glo","iqos"]

def get_word():
    computer = random.choice(word)
    return computer

def hided_word(get_word):
    for element in computer:
        if len(element)>0:
            return len(element)*"_"

def try_word(get_word,hided_word):
    try_1 = 0
    letter = input("write some letter:")
    while letter<12:
        tr1+=1
        for letter, item in enumerate(computer):
            if item == enumerate(computer):
                computer[item]=letter
            else:
                return "you are wrong, try again"

def main():
    get_word
    hided_word(get_word)
    try_word(get_word,hided_word)
        

    




         

