# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

from random import randint

print('Введите количество элементов списка:', end = ' ')
n = int(input())

numbers = list()
for i in range(0, n):
    numbers.append(randint(-100, 100))

print(f'Список из {n} элементов:')
print(numbers)