# task 1

# substring_search = lambda substring, line: substring in line
#
# substring_text = input("Введите текст подстроки: ")
# line_text = input("Введите текст строки: ")
#
# result = substring_search(substring_text, line_text)
# print(result)


# task 2

# chet_number = lambda num: not num % 2
# print(chet_number(8))


# task 3

# check_and_greet = lambda name: f"Привет, {name}!" if name and name[0].isupper() else "Неверное имя."
#
# # Пример использования
# input_name = input("Введите ваше имя: ")
#
# result = check_and_greet(input_name)
#
# print(result)


# task 4

# def digits(n: int) -> str:
#     if n < 10:
#         return str(n)
#     return str(n % 10) + " " + digits(n // 10)
#
#
# number = int(input("Введите натуральное число: "))
# result = digits(number)
# print(result)


# task 5

# def is_power(n: int) -> int:
#     if n == 1:
#         return True
#     elif n % 2 != 0 or n < 1:
#         return False
#     else:
#         return is_power(n // 2)
#
#
# number = int(input("Введите натуральное число: "))
# result = is_power(number)
# print(result)


# task 6
#
# def sum_of_digits(n: int) -> int:
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
#
#
# number = int(input("Введите натуральное число: "))
# result = sum_of_digits(number)
# print(f"Сумма цифр числа {number}: {result}")


# task 7

# import time

# def print_numbers() -> int:
#     for number in range(1, 101):
#         print(number)
#
#
# def modify_print_numbers(fun: callable) -> callable:
#     def inner():
#         stat = time.time()
#         number = fun()
#         end = time.time()
#         total = end - stat
#         return print(f"Программа выполнилась за {total}")
#     return inner


# result = modify_print_numbers(print_numbers)
# print(result())


# task 8

# def password_decorator(create_password_func: callable) -> callable:
#     def inner():
#         correct_password = create_password_func()
#         user_input = input("Введите пароль еще раз для проверки: ")
#         if user_input == correct_password:
#             print("Пароль верный. Добро пожаловать!")
#         else:
#             print("Неверный пароль. Доступ запрещен.")
#     return inner


# def create_password():
#     new_password = input("Введите новый пароль: ")
#     return new_password


# decorated_function = password_decorator(create_password)
# decorated_function()
