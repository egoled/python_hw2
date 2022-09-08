# ЗАДАЧА 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# РЕШЕНИЕ
# n = float(input('Введите число: '))
# sum = 0
# if n<0:
#     n *= -1
# for i in str(n):
#     if i !='.':
#         sum += int(i)
# print(f'Сумма цифр вещественного числа {n} равна {sum}')


# ЗАДАЧА2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# РЕШЕНИЕ
# N = int(input('Введите число: '))
# List=[]
# factorial = 1
# for i in range(1, N+1):
#     factorial *=i
#     List.append (factorial)
# print(List)


# ЗАДАЧА3
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# РЕШЕНИЕ
# n = int(input('Задайте длину последовательности чисел: '))
# numbers = {}
# for i in range(1, n + 1):
#     numbers[i] = round((1 + 1 / n)**n, 2)
# print (numbers)
# print(sum(numbers))


# ЗАДАЧА 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# РЕШЕНИЕ - не работает)

# N = int(input('Задайте число элементов списка: '))
# new_list = []
# import random
# for i in range(N):
#     new_list.append(random.randint(-N, N))
# text = open('file.txt', 'r')
# mult = 1
# for i in text.read():
#     mult = mult * new_list[int(i)]
# print(new_list) 
# print(mult)



# ЗАДАЧА 5
# Реализуйте алгоритм перемешивания списка.

# РЕШЕНИЕ
# new_list = [1, 8, 'python', 0.43]
# print (new_list)
# import random
# random.shuffle(new_list)
# print (new_list)