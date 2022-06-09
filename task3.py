# Подсчитать сумму цифр в вещественном числе.

print('Введите вещественное число: ', end = '')
number = float(input())
number_int = int(str(number).replace('.', ''))
sum = 0

while number_int != 0:
    sum += number_int % 10
    number_int //= 10

print(f'Сумма цифр вещестdенного числа {number} = {sum}')
