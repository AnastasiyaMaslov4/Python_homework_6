# Задайте список из n чисел последовательности (1 + 1/n)^n
# и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите число: "))

result_list = [(1 + 1 / i) ** i for i in range(1, n + 1)]

num_list = list(enumerate(result_list))

print(num_list)
print("Сумма: ", sum(result_list))