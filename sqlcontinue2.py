import psycopg2

class MEGA:

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
        CREATE TABLE NEW_PRODUCTS
        (ID INT PRIMARY KEY,
        PRODUCT_NAME VARCHAR(100) NOT NULL,
        MANUFACTURER VARCHAR(100) NOT NULL,
        Memory INT,
        PRICE INT);
        """)
        self.con.commit()
        print("Table is created")

    def add_phones(self):
        serial_num1 = int(input("\nВведите номер серий:"))
        phone_name = input("\nВведите модель телефона:")
        phone_manufacturer = input("\nВведите компанию производитель:")
        phone_memory = int(input("\nВведите память телефона:"))
        phone_price = int(input("\nВведите цену:"))
        self.cur = self.con.cursor()
        self.cur.execute(f"""
        INSERT INTO NEW_PRODUCTS(ID,PRODUCT_NAME,MANUFACTURER,MEMORY,PRICE) VALUES( 
        {serial_num1},'{phone_name}','{phone_manufacturer}', {phone_memory} , {phone_price})

        """)
        self.con.commit()
        print("phones are added")

    def view(self):
        self.cur = self.con.cursor()
        self.cur.execute(
            "SELECT * FROM NEW_PRODUCTS")
        rows = self.cur.fetchall()
        for row in rows:
            print("ID:", row[0], "|", "PRODUCT_NAME:", row[1], "|", "MANUFACTURER:", row[2], "|", "MEMORY:", row[3], "|", "PRICE:", row[4])
        self.con.commit()


    def update(self):
        new_price = int(input("\nВведите новую цену:"))
        which_phone = int(input("\nВведите номер серий телефона, который хотите обновить:"))
        self.cur = self.con.cursor()
        self.cur.execute(f"""
        UPDATE NEW_PRODUCTS set PRICE = {new_price}  WHERE id = {which_phone}""")
        self.con.commit()

    def utilize(self):
        del_phone = input("\nВведите номер серий телефона, который хотите удалить:")
        self.cur = self.con.cursor()
        self.cur.execute(
        f"DELETE FROM NEW_PRODUCTS WHERE id = {del_phone}"  )
        self.con.commit()

    def main(self):
        print("\nПриветствую, какие действия желаете?")
        print("[1] = Просмотр таблицы")
        print("[2] = Добавить новый продукт")
        print("[3] = Удалить продукт")
        print("[4] = Изменение цены продукта")
        
        self.staff = int(input("\nВведите цифру запроса:"))
        if self.staff == 1:
            self.view()
        elif self.staff == 2:
            self.add_phones()
        elif self.staff == 3:
            self.utilize()
        elif self.staff == 4:
            self.update()
    
        try:
            if self.staff > 4:
                raise IndexError
        except IndexError as indexerror1:
            print("Введите от 1 до 4", indexerror1)
        # try:
        #     raise TypeError        
        # except TypeError as typeerror2:
        #     print("Вводите только цифры")
        
        self.choice = input("\nХотите продолжить, введите yes/no:?")
        if self.choice == "yes":
            return self.main()
        elif self.choice == "no":
            print("\nДосвидания")
            exit()
        else:
            print("Напишите yes/no")
            return self.choice()

phones = MEGA()
phones.main()
