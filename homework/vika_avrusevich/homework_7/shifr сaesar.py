# Шифр цезаря
#
# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
#
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
#
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
# Знаки препинания должны сохраниться.


def encypt_func(text, step):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for i in range(len(text)):
        if text[i].isalnum():
            result += alpha[(alpha.find(text[i]) + step) % (len(alpha))]
        else:
            result += text[i]
    return result


user_text = str(input('Введите текст для шифровки: '))
user_step = int(input('Введите шаг шифровки      : '))

print(f'\nИсходный текст      : {user_text}'
      f'\nШаг                 : {str(user_step)}'
      f'\nЗашифрованный текст : {encypt_func(user_text, user_step)}')

