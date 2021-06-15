# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ

import random

num = random.randint(0, 100)
print(num)
i = 1
while i <= 10:
    print(f'Попытка №{i} из 10')
    user_number = int(input('Введите число от 1 до 100: '))
    if user_number == num:
        print('Поздравляю, Вы угадали загаданное число!')
        break
    elif user_number > num:
        print(f'Ваше число {user_number} больше загаданного')
    else:
        print(f'Ваше число {user_number} меньше загаданного')
    i += 1
if i > 10:
    print(f'Не угадано! Загаданное число {num}')
