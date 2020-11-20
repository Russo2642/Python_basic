list1 = ["png","jpeg","jpg","svg"]

user_input = input("vvedite nazvanie i format:").lower().split(".")

if user_input[-1] in list1:
    print("verno")
else:
    print("neverno")

