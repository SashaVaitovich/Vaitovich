# task 1

# numbers = (6, 2, 7, 8)
#
# for number in numbers:
#     sum_of_divisors = 0
#     for i in range(1, number):
#         if number % i == 0:
#             sum_of_divisors += i
#     if sum_of_divisors == number:
#         print(number)



# task 2

# numbers_tuple = (5, -2, -2, 7, -8, -9, 1)
# sign_changes_count = sum(1 for i in range(1, len(numbers_tuple)) if (numbers_tuple[i-1] < 0) != (numbers_tuple[i] < 0))
#
# print(sign_changes_count)



# task 3

# list_1 = input("Список №1: ").split()
# list_2 = input("Список №2: ").split()
#
# unique_elements = set(list_1) - set(list_2)
# print(unique_elements)
#
# if not unique_elements:
#     print("Нет элементов, которые не входят во второй список.")
# else:
#     min_element = min(unique_elements)
#     print("Наименьший элемент, который не входит во второй список:", min_element)



# task 4

# numbers = [16, 19, 42, 8, 122]
# result_list = []
#
# for num in numbers:
#     result_list.append(num)
#     if num % 2 == 0:
#         reversed_num = int(str(num)[::-1])
#         result_list.append(reversed_num)
# print("Результат:", result_list)



# task 5

# numbers_list = [5, 2, 4, 5, 1, 2]
# count_dict = {}
#
# for element in numbers_list:
#     if element in count_dict:
#         count_dict[element] +=1
#     else:
#         count_dict[element] = 1
# print(count_dict)



# task 6

# original_list = [7, 4, 1]
# result_list = []
#
# for number in original_list:
#     result_list.append(number)
#     if number != original_list[-1]:
#         result_list.append(0)
# print(result_list)



# task 7

# input_str = input("Введите последовательность чисел через пробел: ")
# numbers = input_str.split()
# seen_numbers = set()
#
# for number in numbers:
#     number = int(number)
#     if number in seen_numbers:
#         print("YES")
#     else:
#         print("NO")
#         seen_numbers.add(number)



# task 8

# n = int(input())
# all_nums = set(range(1, n + 1))
# possible_nums = all_nums
# while True:
#     guess = input()
#     if guess == 'HELP':
#         break
#     guess = {int(x) for x in guess.split()}
#     answer = input()
#     if answer == 'YES':
#         possible_nums &= guess
#     else:
#         possible_nums &= all_nums - guess
#
# print(' '.join([str(x) for x in sorted(possible_nums)]))



# task 9

# synonym_dictionary = int(input("Введите слово и через пробел синоним:"))
# d = {}
# for i in range(synonym_dictionary):
#     first, second = input().split()
#     d[first] = second
#     d[second] = first
# print(d[input("Введите слово к которому нужен синоним:")])



# task 10

# phone_book = {}
#
# while True:
#     entry = input().strip()
#     if entry == '.':
#         break
#     name, *number = entry.split()
#     if number:
#         phone_book[name] = ' '.join(number)
#     else:
#         print(f"{name}: {phone_book.get(name, 'Контакт не найден.')}")
# print("Список контактов:")
# for name, number in phone_book.items():
#     print(f"{name}: {number}")
