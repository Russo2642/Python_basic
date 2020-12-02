##Реализовать класс Person, у которого должно быть два публичных поля: age и name. 
#Также у него должен быть следующий набор методов: know(person), который позволяет 
#добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека

#*ЗАДАЧА 2:
#Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
#Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

#*ЗАДАЧА 3:
#Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
#Другие - нет. За что будет отвечать метод is_dangerous(animal)

class Person:
    
    def __init__(self, age, name):
        self.age = age
        self.name = name

        print('self.age, self.name')

    def know(self,person):
        self.spisok.append(person)
        print(self.spisok)

    def is_known(self,person):
        if person in self.spisok
        else:
            print('not')
        break
    

    
 #   def is_known(person):


#2

class Printer:
    def log(*values)

class FormattedPrinter:
    def log(*values)

print(f"FormattedPrinter:"{log(*values)} )

#3

class Animal:
    def __init__(self, home, is_dangerous):
        self.home = home
        self.is_dangerous = is_dangerous
        print('self.home, self.is_dangerous')

class Human:
    def __init__(self, name):
        self.name = name
        print('self.name')
