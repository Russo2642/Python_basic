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
    # print('-'*len(list1))
    skritiy_text = list('_'*len(list1))
    print(skritiy_text)
   
    spisok_vvoda = []
    prav_vvod_bukva = input()

    def prav_vvod(list1,skritiy_text,spisok_vvoda,prav_vvod_bukva):
        spisok_vvoda.append(prav_vvod_bukva)
    prav_vvod(list1,skritiy_text,spisok_vvoda,prav_vvod_bukva)


    def graphika(skritiy_text,spisok_vvoda,list1,prav_vvod_bukva):
        # result = list(set(list1) and set(spisok_vvoda))
        # prav_vvod_bukva_sp = list(prav_vvod_bukva)
        # skritiy_text.insert(,prav_vvod_bukva_sp)
        for i in list1:
            if prav_vvod_bukva == list1:
                print('ti ugadal bukvu')
                print(skritiy_text.insert)
                result = set(list1) and set(spisok_vvoda)
                print(result.index)
                print(skritiy_text.insert(result.index,prav_vvod_bukva))
            

    graphika(skritiy_text,spisok_vvoda,list1,prav_vvod_bukva)

    def is_game_finished(list1,spisok_vvoda):
        list1 == spisok_vvoda
        if list1 == spisok_vvoda:
            print(list1)
            print('molodets')
    is_game_finished(list1,spisok_vvoda)

    


    def main():
        t = 0
        while not is_game_finished:
            prav_vvod_bukva = input()
            spisok_vvoda = []
            spisok_vvoda = prav_vvod()
        while t < 10:
            prav_vvod_bukva = input()
            t = t + 1
        if spisok_vvoda == list1:
            print('ti viigral')
            exit
    main()



          


    
        



























    #     t = 0
    #     while t < 10:
    #         if prav_vvod_bukva in list1:
    #             print('molodets')
    #             t = t +1
    #             spisok_vvoda.append(prav_vvod_bukva)
                
    #         elif prav_vvod_bukva not in list1:
    #             print('try again')
    #             print(str(10 - 1) ,'попыток осталось')
    #             t = t + 1

    #         elif len(result(set(list1 and set(spisok_vvoda))))== len(list1):
    #             print('ТЫ УГАДАЛ СЛОВО')
    #             t = 10
    #     print(spisok_vvoda)
    # prav_vvod(list1,skritiy_text)

    # def main():
    # main()
      
      
      
      
      
      
      
      
      
        # prav_vvod_bukva = input()
        
       
    #       
            
        
    #         if prav_vvod_bukva in list1:
    #             print("molodets")
    #             t = t + 1
            
    #             # print(skritiy_text.insert(index(list1),prav_vvod_bukva))
    #         elif prav_vvod_bukva not in list1:
    #             print('try again,this letters doesn\'t belong to word')

    #             t = t + 1
    #         elif len(result=list(set(list_vvod) and set(list1))) == len(list1):
    #             print('ti viigral')

    #             break 
    #     print(list_vvod)
    # prav_vvod(list1,skritiy_text)
    # def main():
    # main()
        




        
        
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