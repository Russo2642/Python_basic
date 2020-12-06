conv_ = ((10, 'X'), (9, 'IX'), (8, 'VIII'), (7, 'VII'), (6, 'VI'), (5, 'V'), (4, 'IV'), (3, 'III'), (2, 'II'), (1, 'I'))

def arab_to_roman( number ):
    if number <= 0: return ''

    ret = ''
    for arab, roman in conv_:
        while number >= arab:
            ret += roman
            number -= arab

    return ret

def roman_to_arab( txt ):
    txt = txt.upper()
    ret = 0
    for arab, roman in conv_:
        while txt.startswith( roman ):
            ret += arab
            txt = txt[ len(roman): ]
    return ret

for i in ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ):
    arab = arab_to_roman(i)
    roman = roman_to_arab(arab)
    print (i, arab, roman)