# task 1

# a = int(input("Введите число a:"))
# b = int(input("Введите число b:"))
# c = int(input("Введите число c:"))

# if a<0 or b<0 or c<0:
#     print("True")
# else:
#     print("False")



# task 2

# n = int(input("Введите целое число n:"))
# k = int(input("Введите целое число k:"))
#
# if n % 2 == k % 2:
#     print(True)
# else:
#     print(False)



# task 3

# a = int(input("Целое число a:"))
# b = int(input("Целое число b:"))
# c = int(input("Целое число c:"))
# count = 0
#
# if a % 2 == 0:
#     count += 1
# if b % 2 == 0:
#     count += 1
# if c % 2 == 0:
#     count += 1
# print("Количество четных чисел:", count)



# task 4

# double_number = input("Введите двузначное число:")
#
# if len(double_number) == 2 and double_number.isdigit():
#     digit_sum = int(double_number[0]) + int(double_number[1])
#     if len(str(digit_sum)) == 2:
#         print("Сумма цифр является двузначным числом.")
#     else:
#         print("Сумма цифр не является двузначным числом.")
# else:
#     print("Введенное значение не является двузначным числом.")



# task 5

# for _ in range(20):
#     print("10")



# task 6

# number_n = int(input("Введите число n:"))
#
# for cube_of_numbers in range(1, number_n+1):
#     print(cube_of_numbers**3)



# task 7

# result = 1
# for i in range(5, 21):
#     result *= i
# print(result)



# task 8

# n = int(input("Введите число n: "))
# i = 1
# while i**2 < n:
#     print(i**2)
#     i += 1



# task 9

# n = int(input("Введите число n: "))
# n_str = str(n)
# min_digit = 9
# for digit_str in n_str:
#     digit = int(digit_str)
#     if digit < min_digit:
#         min_digit = digit
# print(min_digit)



# task 10

# year = int(input("Введите год:"))
#
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("Високосный")
# else:
#     print("Не високосный")
