# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

list_size = int(input("Введите размер списка: "))
new_list = [random.randint(1, 10) for i in range(list_size) ]

print(new_list)

nums_sum = 0
index = 0

for index in range(list_size):
    if index % 2 != 0:
        nums_sum += new_list[index]
    else:
        continue

print(f"Сумма равна {nums_sum}")