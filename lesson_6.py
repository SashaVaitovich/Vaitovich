# task 1

# print([num**2 for num in range(1, 11)])


# task 2

# print([num for num in range(100, 1000) if not num % 5 and not num % 3])


# task 3

# num_1, num_2, num_3 = list(map(int, input("Введите числа через пробел: ").split()))
# print([degree_of_number ** num_3 for degree_of_number in range(num_1, num_2 + 1)])


# task 4

# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# if len(numbers) == 1:
#     print(numbers[0])
# elif len(numbers) == 2:
#     print("Сумма двух чисел:", numbers[0] + numbers[1])
# else:
#     cum_num = numbers[-1:] + numbers + numbers[:1]
#     print(*[a + b for a, b in zip(cum_num, cum_num[2:])])


# task 5
# def min_number(num_1: int, num_2: int) -> int:
#     return min(num_1, num_2)
#
#
# result = min_number(min_number(6, 7), min_number(9, 1))
# print(f"Минимальное число из 4-ых чисел: {result}")


# task 6
#
# def distance(x1: float, y1: float, x2: float, y2: float) -> float:
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
#
# x1 = float(input("Введите x-координату первой точки: "))
# y1 = float(input("Введите y-координату первой точки: "))
# x2 = float(input("Введите x-координату второй точки: "))
# y2 = float(input("Введите y-координату второй точки: "))
#
# distance = distance(x1, y1, x2, y2)
# print(f"Расстояние между точками A и B: {distance}")


# task 7

# def fib(n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
#
# n = int(input("Введите неотрицательное целое число n: "))
# result = fib(n)
# print(f"{n}-е число Фибоначчи: {result}")


# task 8

# def closest_mod_5(x: int) -> int:
#     y = x + (5 - x % 5) % 5
#     return y
#
#
#
# number = int(input("Введите целое число x: "))
# result = closest_mod_5(number)
# print(f"Ближайшее число, кратное 5, большее или равное {number}: {result}")


# task 9

# def modify_list(lst: list):
#     i = 0
#     while i < len(lst):
#         if not lst[i] % 2:
#             lst[i] //= 2
#             i += 1
#         else:
#             del lst[i]
#
#
# my_list = list(map(int, input().split()))
# modify_list(my_list)
# print(my_list)
