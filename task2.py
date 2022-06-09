# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

print('Введите первую строку:', end = ' ')
first_string = input()
print('Введите вторую строку:', end = ' ')
second_string = input()

# for i in range(0, len(first_string) + 1):
print(f'Вторая строка содержится в первой {first_string.count(second_string)} раз(а)')