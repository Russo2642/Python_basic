import random

try_try = 0
start_game = input("do you want to start game, yes or no?:")
if start_game.lower()=="yes":
    print("lets go")
else:
    print("goodbye")
    exit()
    
computer = random.randint(0,100)

while try_try<6:
    try_try+=1
    user_try = int(input("\nchoose a number between 0 and 100:"))
    if user_try>computer:
        print("\nbigger than computer")
    if user_try<computer:
        print("\nsmaller than computer")
    
    
    if user_try==computer:
        print("congratulations, you won")
        break
if user_try!=computer:
    print("\nyou loose my friend")
    print("\nanswer is:" ,computer)





