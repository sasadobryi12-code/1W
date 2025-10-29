# Задание 1 ---------------------------------------------

# def task_01_func(year):
#     if year % 4 == 0:
#         if year % 100 != 0:
#             return 'YES'
#         else: 
#             if year % 400 == 0:
#                 return 'YES'
#             else:
#                 return 'NO'
#     else:
#         return 'NO'

# n = int(input())
# print(task_01_func(n))

# Задание 2 ---------------------------------------------

# Решение 1

# def task_02_func(number):
#     cnt = 0
#     while number > 0:
#         number = number // 10
#         cnt = cnt + 1 
#     return cnt

# n = int(input())
# print(task_02_func(n))

# Решение 2

# def task_021_func(number):
#     s = str(number)
#     return len(s)
# n1 = input()
# print(task_021_func(n1))

# Задание 3 ---------------------------------------------

#  Первое решение

# n = int(input())
# p_factorial = 1
# p_factorial_sum = 0
# for i in range(1,n+1):
#     p_factorial *= i
#     p_factorial_sum += p_factorial
# print(p_factorial_sum)

#  Второе решение

# def task_03_func(n):
#     s, p = 0, 15
#     for i in range(1, n+1):
#         p *= i
#         s += p
#     return s
# print(task_03_func(4))

#  Третье решение

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    

# def sum_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return factorial(n) + sum_factorial(n-1)

# print(sum_factorial(4))

# Задание 4 ---------------------------------------------

# Решение 1 

# def task_04_func(s):
#     n_r = ''.join(reversed(n))
#     if n_r == n:
#         return 'Слово является полиндромом'
#     else:
#         return 'Слово не является полиндромом'

# n = str(input())
# print(task_04_func(n))

# Решение 2

# def task_041_func(s):
#     s_lower = s.lower()
#     return s_lower == s_lower[::-1]

# n = str(input())s = input()
# polindrom = True
# dlin = len(s)
# for i in range(dlin//2):
#     if s[i] != s[dlin - i -1]:
#         polindrom = False
#         break
# if polindrom:
#     print('Слово является полиндромом')
# else:
#     print('Слово не является полиндромом')
# print(task_041_func(n))

# Решение 3

# s = input()
# polindrom = True
# dlin = len(s)
# for i in range(dlin//2):
#     if s[i] != s[dlin - i -1]:
#         polindrom = False
#         break
# if polindrom:
#     print('Слово является полиндромом')
# else:
#     print('Слово не является полиндромом')

# Задание 5 ---------------------------------------------

# Решение 1

# def task_05_func(text):
#     words = text.split(' ')
#     wourd_counter = {}
#     for word in words:
#         if word in wourd_counter:
#             wourd_counter[word] += 1
#         else:
#             wourd_counter[word] = 1
#     return wourd_counter
# word_input = input("Введите текст: ")
# print(task_05_func(word_input))

#  Решение 2

# from collections import Counter

# word_input = input("Введите текст: ")
# print(dict(Counter((word_input.split(' ')))))

# Задание 6 ---------------------------------------------

# def task_06_func(input_str, input_char):
#     first = None
#     last = None
#     count = 0

#     for i, char in enumerate(input_str):
#         if char == input_char:
#             if first is None:
#                 first = i
#             last = i
#             count += 1

#     if count == 0:
#         return (None, None)
#     elif count == 1:
#         return (first, None)
#     else: 
#         return (first, last)

# print(task_06_func("hello", "l"))   # (2, 3)
# print(task_06_func("hello", "o"))   # (4, None)
# print(task_06_func("hello", "x"))   # (None, None)
# print(task_06_func("a", "a"))       # (0, None)
# print(task_06_func("aba", "a"))     # (0, 2)
    
# Задание 7 ---------------------------------------------

# Решение 1 

# def struc(n):
#     b = [x**2 for x in n if x >= 0]
#     b.sort(reverse=True)
#     return b

# a = [1, 2, -3, 4, 5, -1, -2, 3, -4, -5]

# print(struc(a))

# Решение 2

# import numpy as np

# def sitruc1(n):
#     b = np.copy(n).tolist() 
    
#     i = len(b) - 1
#     while i >= 0:
#         if b[i] < 0:
#             del b[i]       
#         else:
#             b[i] = b[i] ** 2  
#         i -= 1
    
#     b.sort(reverse=True)    
#     return b
# a = [1, 2, -3, 4, 5, -1, -2, 3, -4, -5]
# print(sitruc1(a))


# Решение 3

# def stucture(n):
#     b = list(filter(lambda x: x >= 0, a))
#     c = list(map(lambda x: x **2 ,b))
#     c.sort(reverse=True)
#     return c

# a = [1, 2, -3, 4, 5, -1, -2, 3, -4, -5]
# print(stucture(a))

# Задание 11 ---------------------------------------------

# def task_11_func(first_list, second_list):
#     second_set = set(second_list)
#     filtered = filter(lambda x: x not in second_set, first_list)
#     return list(dict.fromkeys(filtered))

# print(task_11_func([1, 2, 2, 3, 4], [2, 4]))  # [1, 3]
# print(task_11_func([5, 6, 7], [1, 2]))        # [5, 6, 7]
# print(task_11_func([1, 1, 1], [1]))           # []
# print(task_11_func([3, 1, 3, 2], [3]))        # [1, 2]
