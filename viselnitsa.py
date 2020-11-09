import random
print("приветствую друже, давай поигаем в висельницу")
print( "_" * 20 )
print("""правила просты : просто угадай слова
каждая верная буква будет открываться,
а неверная будет снижать количество попыток
которых у тебя 10 """)   
print('_' * 20)
themes = ['auto','techno','food','jobs','countries']
print('enter index 1-5')
index0 = int(input())
index1 = index0 - 1
if index1 == 0:
    print('your theme is:')
    print(str(themes[index1]))
    print('_'*20)
    auto = ['mercedes','bugatti','smart','toyota','renault','jaguar','rangerover','hummer','engine','breakes','petrol','mazda']
    word = random.choice(auto)
    list1 = list(word)
    print(len(list1))
    print("~"*20)
    print('-'*len(list1))
    skritiy_text = list('-'*len(list1))
    print(skritiy_text)
    def prav_vvod(list1,skritiy_text):
        prav_vvod_bukva = input()
        i = [0,1,2,3,4,5,6,7,8,9,10]
        if prav_vvod_bukva == list1[list1.index(prav_vvod_bukva)]:
            print(skritiy_text.insert(list1.index(prav_vvod_bukva),prav_vvod_bukva))
    prav_vvod(list1,skritiy_text)
        
        
        # for bukvi in list1: 
        # if bukva_vvod == list1:
        #     print(bukva_vvod)
        # elif bukva_vvod != list1:
        #     print('try again')
    
    
    
    
    
    
    
    
    
    
    # def zamenabukv(list1):
    #     vvodbukvi = input()
    #     if vvodbukvi == list[index1]:
    #         print(vvodbukvi)
    # zamenabukv(list1)

    
  
  
  
  
  
  
  
  
  
  
  
    # for leters in word:
    #     leters = '*'
    #     print(leters)
    #     leterugadal = input()
    #     if leterugadal == leters:
    #         print(word)
    # # print(auto_list)
    # print('_'*20)