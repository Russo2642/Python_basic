right_answers = 0
wrong_answers = 0


first = {"what is the name of course?":"python"}
a = input("what is the name of course?:")
print('правильный ответ:"{}"'.format(first["what is the name of course?"]))
if a=="{}".format(first["what is the name of course?"]):
    print("you are right")
    right_answers=right_answers+1
else:
    print("fault")
    wrong_answers=wrong_answers+1

second = {"what is the name of teacher?":"Ruslan"}
b = input("\nwhat is the name of teacher?:")
print('правильный ответ:"{}"'.format(second["what is the name of teacher?"]))
if b=="{}".format(second["what is the name of teacher?"]):
    print("you are right")
    right_answers=right_answers+1
else:
    print("fault")
    wrong_answers=wrong_answers+1

third = {"who says meow?":"cat"}
c = input("\nwho says meow?:")
print('правильный ответ:"{}"'.format(third["who says meow?"]))
if c=="{}".format(third["who says meow?"]):
    print("you are right")
    right_answers=right_answers+1
else:
    print("fault")
    wrong_answers=wrong_answers+1

print("\ntotal of right answers:", right_answers)
print("\ntotal of wrong answers", wrong_answers)