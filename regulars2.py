import re

domain = "www.site.com"

print(re.findall(r'www.\w*.com',domain))


history_comment = "20 век был более опасным, чем 19 век"

print(re.findall(r"\d+\sвек",history_comment))

print(re.findall(r'^\d+\sвек',history_comment))

print(re.findall(r"\d+\sвек$",history_comment))


websites = "www.101.com www.google.com"

print(re.findall(r"www.\d*\w*.com",websites))


passwords = ["Apple34!rose","My87hou#4S","abc123"]

regex_ = r"[\w*!#$%&]{8,20}"

for i in passwords:
    if re.match(regex_,i):
        print(f"Password {i} is correct")


string_01 = "Жизнь - это то, что с тобой происходит, пока ты строишь планы. Джон Ленон."

# user = input("put some letter to find:")

# find_1 = r"\b\suser\w*\b"

# print(re.findall(find_1,string_01))

print(re.findall(r"\bп\w*\b", string_01))


prices = "RUB4.44, RUB10.88, EURO0.99, RUB99.99"

print(re.findall(r"RUB\d+.\d+",prices))


flight = "Boarding pass: LA4214 AER-CDB 06NOV" # способ группировки 

regex_flight = r'([A-Z]{2})(\d{4})\s([A-Z]{3}-[A-Z]{3})\s(\d{2}[A-Z])'

flight_result = (re.findall(regex_flight,flight))

print(flight_result)

email_1 = "k_elaman@mail.ru"
regex_email = r'[\w*@-_.]{6,20}.[a-z]{2,8}'
for element in email_1:
    if re.match(regex_email,email_1):
        print(f"accepted, {email_1}")
    else:
        print("try again")


print(re.findall(regex_email,email_1))

phone_num =  "+7-(701)-186-82-95"

regex_num = r'([+\d*]{2})-([()\d*]{5})-([\d*]{3}-[\d*]{2}-[\d*]{2})'

for elements in phone_num:
    if re.match(regex_num,phone_num):
        print(f"phone is accepted {phone_num}")
    else:
        print("try again")

print(re.findall(regex_num,phone_num))
