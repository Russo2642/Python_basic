import psycopg2
import re

class Mailbox:


    def __init__(self):
        self.con = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = "Tualatinx33",
            host = "localhost",
            port = "5432"
        )
        self.con.commit()
        print("DATABASE IS CONNECTED")

    def cr_table(self):
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE USERS 
        (ID INT,
        NAME VARCHAR(100) NOT NULL,
        EMAIL VARCHAR(100) NOT NULL,
        PHONE VARCHAR(100) NOT NULL);
        """)
        self.con.commit()
        print("table is created")

    def add_info(self):
        self.cur = self.con.cursor()
        put_id = int(input("введите ID участника: "))
        put_name = input("введите имя участника: ")
        email_1 = input("введите почту (доступные символы: -,_,. ")
        phone_num = input("введите номер телефона по формату: +7-(701)-186-82-95 ")
        regex_email = r'[\w*@-_.]{6,20}.[a-z]{2,8}'
        regex_num = r'([+\d*]{2})-([()\d*]{5})-([\d*]{3}-[\d*]{2}-[\d*]{2})'

        if re.match(regex_email,email_1) and re.match(regex_num,phone_num):
            self.cur.execute(f"""
            INSERT INTO USERS (ID,NAME,EMAIL,PHONE) VALUES
            ({put_id}, '{put_name}', '{email_1}', '{phone_num}')""")
        else:
            print("Введите почту или телефон корректно")

        self.con.commit()
    

    def view(self):
        self.cur = self.con.cursor()    
        self.cur.execute(
        "SELECT * FROM USERS")
        row = self.cur.fetchall()
        for rows in row:
            print("ID", rows[0], "NAME", rows[1], "EMAIL", rows[2], "PHONE", rows[3])
        self.con.commit()

    def main(self):
        print("Какие действия желаете?")
        print("[0] = Просмотр таблицы пассажиров")
        print("[1] = Добавление нового пассажира")

        self.staff = int(input("Введите желаемые действия:"))

        if self.staff == 0:
            self.view()
        elif self.staff == 1:
            self.add_info()

        self.choice = input("\nХотите продолжить, введите yes/no:?")
        if self.choice == "yes":
            return self.main()
        elif self.choice == "no":
            print("\nДосвидания")
            exit()
        else:
            print("Напишите yes/no")
            return self.choice()



mail = Mailbox()
mail.main()