#string types:
#print("this is string.")
#print('this is also string.')

#print("'")
#print('a'=='a')
#print('a'== 'b')
#print('we are equal'=="we are equal")


#print('я русская строка')
# imenno s tremya odinarnymi ili dvoinymi kovychkami
#print('''
#This string contains multiline
    #text. And extra spaces.
    #''')


#print("my name is {}". format('Yela'))

#print("здравствуйте, расскажите о себе?")
#a=input("как вас зовут?:")
#b=input("сколько вам лет?:")
#c=input("откуда вы?:")

#print("{},\n\t{},\n\t{}".format(a,b,c))


#a=1
#b=2
#c=3

#if a>b or b>c or a>c:
    #print("a bolshe b")
#else:
    #print("a samoe malenkoe, c samoe bolshoe")

#print("check your information:")
#print("your name:{},\nyour age:{},\nyour city:{}". format(a,b,c))


a=input("a:")
b=input("b:")
c=input("c:")

if a>b or a>c or b>c:
    print("a bolshe vseh")
else:
    print("a menshe vseh, no c bolshe vseh")