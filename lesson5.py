# try:
#     1/0
# except:
#     print("na 0 delit nelzya")

# try:
#     1/0
# except ZeroDivisionError:
#     print("na 0 delit nelzya")


# try:
#     d = {"key":23}
#     print(d['does not exist'])
# except ZeroDivisionError:
#     print("this won't be called")


# try:
#     d = {"key":23}
#     print(d['does not exist'])
# except KeyError as e:
#     print("got it", e)


try:
    raise ValueError("custom message")
except ValueError as e:
    print("message is", e)

try:
    raise ValueError()
except ZeroDivisionError:
    print("divided by zero")
except AttributeError:
    print("Key is missing")
except Exception as ex:
    print("i dont know what is going on")
    print(ex)



try:
    print("fine")
except KeyError:
    print("Nope")
else:
    print("else clause")


try:
    print(1/0)
except ZeroDivisionError:
    print("0!")
finally:
    print("i will be here anyway")