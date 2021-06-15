# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр

user_number = 12345  # int(input('Введите число: '))
max_num = 0
sum_num = 0

while user_number > 0:
    digit = user_number % 10  # находим последнюю цифру
    sum_num = sum_num + digit
    if digit > max_num:
        max_num = digit
    user_number = user_number // 10  # удаляем последнюю цифру
print(f'Максимальное число: {max_num}\nСумма введенных чисел: {sum_num}')



# max_number = 0
# max_sum = 0
# for i in list_number:
#     if sum_numbers(i) > max_sum:
#         max_number = i
#         max_sum = sum_numbers(i)
#
# print(f'У числа {list_number} была наибольшая сумма цифр - {max_sum}')