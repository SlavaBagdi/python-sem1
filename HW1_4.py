# Задание 4:
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
    print('Ошибка! Пожалуйста, измените ввод номера четверти!')
elif n == 1:
    print('x > 0 and y > 0')
elif n == 2:
    print('x < 0 and y > 0')
elif n == 3:
    print('x < 0 and y < 0')
elif n == 4:
    print('x > 0 and y < 0')
