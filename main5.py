# 1) RLE-сжатие – один из самых простых методов сжатия строки, основанный на 
# сокращении подстрок, состоящих из одинаковых символов. Сжатие осуществляется 
# следующим образом: Строка разбивается на минимальное количество подстрок, 
# состоящих из одинаковых символов. Например, abbcaaa превращается в строки 
# a, bb, c, aaa. Каждая из полученных строк превращается в строку, состоящую из
# числа и буквы. Числом является количество повторений символа в этой строке, 
# буква берётся из первого символа обрабатываемой строки. Число не добавляется, 
# если количество символов в строке равно единице. Из предыдущего массива строк 
# мы получаем a, 2b, c, 3a. Затем полученные строки конкатенируются в исходном 
# порядке. В рассмотренном примере в итоге получим a2bc3a.
# Вводится строка, нужно сжать ее по алгоритму, описанному выше.

# def new_str(some_str):
#     newstring = ''
#     i = 0
#     while i < len(some_str):
#         count = 1
#         while i + 1 < len(some_str) and some_str[i] == some_str[i + 1]:
#             count +=1
#             i +=1
#         newstring += str(count) + some_str[i]
#         i +=1
#     return newstring

# some_str = input('')
# print(new_str(some_str))


# 2.Создайте список из случайных чисел. Найдите номер его последнего локального 
#максимума (локальный максимум — это элемент, который больше любого из 
# своих соседей).

# import random
# some_list = []
# count = int(input('Кол-во элементов: '))
# for i in range(count):
#     number = random.randint(1, 10)
#     some_list.append(number)
# some_list = [-1] + some_list + [-1]
# print(some_list)
# for i in range(-2, -(len(some_list)), -1):
#     if some_list[i-1] < some_list[i] > some_list[i+1]:
#         print((len(some_list)-2) + (i+1))
#         break


# 3.Создайте список из случайных чисел. Найдите максимальное количество 
# его одинаковых элементов.

# import random
# some_list = []
# count = int(input('Кол-во элементов: '))
# sum_max = 0
# for i in range(count):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)
# first_max = 0
# for i in set(some_list):
#     if i > first_max:
#         first_max = i
# for i in (some_list):
#     if i == first_max:
#         sum_max +=1
# print('Максимальное число: ', first_max)
# print('Максимальное количество данного элемента: ', sum_max)


# 4.Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2

# import random
# some_list = []
# count = int(input('Кол-во элементов: '))
# for i in range(count):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)
# sorted_list = sorted(some_list)
# print('Первый макимум: ', (sorted_list[-1]))
# print('Второй максимум: ', (sorted_list[-2]))


