#Создайте класс сотрудника Employee. При инициализации класса задается имя сотрудника name и его текущая зарплата salary. Напишите следующие методы:

#Метод up, который увеличивает зарплату сотрудника на 100
#Метод print, который выводит на экран текущую зарплату сотрудника в формате "Сотрудник Иван, зарплата 100"

class Employee:
    #emp_count = 0 #базовый класс сотрудника

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def up (self, name, salary):
        self.name = Ivan
        self.salary = 100
        print("self.name, self.salary")