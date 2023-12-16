# task 1
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# n = 10
# for number in fib(n):
#     print(number)

# task 2

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def simple(n):
#     current_number = 2
#     while current_number < n:
#         if is_prime(current_number):
#             yield current_number
#         current_number += 1
#
#
# n = 20
# generator = simple(n)
#
# try:
#     while True:
#         prime_number = next(generator)
#         print(prime_number)
# except StopIteration:
#     print(f"Простые числа до {n} исчерпаны.")


# task 3

# def is_perfect_number(number):
#     divisors_sum = sum(i for i in range(1, number) if number % i == 0)
#     return divisors_sum == number
#
#
# def perfect_numbers():
#     number = 2
#     while True:
#         if is_perfect_number(number):
#             yield number
#         number += 1
#
#
# for perfect_number in perfect_numbers():
#     if perfect_number < 1000000000:
#         print(perfect_number)
#     else:
#         break


# task 4

# input_str = "Hello {world, this is a {test} string."
#
# start_index = input_str.find('{')
# end_index = input_str.find('}')
# if start_index != -1:
#     if end_index != -1:
#         processed_str = input_str[:start_index] + input_str[end_index + 1:]
#     else:
#         processed_str = input_str[:start_index]
# else:
#     processed_str = input_str
#
# print(f"Processed string: {processed_str}")
#
#
# char_count = {}
# for char in processed_str:
#     if char.isalpha():
#         char_count[char] = char_count.get(char, 0) + 1
#
# most_common_char = max(char_count, key=char_count.get, default=None)
#
# print(f"Most common character: {most_common_char}")

# task 5

# class Server:
#     def __init__(self):
#         self.data = []
#
#     def process_command(self, command):
#         cmd_parts = command.split()
#
#         if not cmd_parts:
#             return self.data
#
#         cmd_type = cmd_parts[0]
#
#         if cmd_type == 'POST':
#             if len(cmd_parts) > 1:
#                 data_to_add = cmd_parts[1]
#                 self.data.append(data_to_add)
#         elif cmd_type == 'GET':
#             if self.data:
#                 print(self.data[-1])
#         elif cmd_type == 'DELETE':
#             if self.data:
#                 deleted_data = self.data.pop()
#         return self.data
#
#
# server = Server()
#
# commands = input("Введите команды (прерывание ввода точкой): ").split(',')
# for command in commands:
#     server.process_command(command.strip())
#
# if server.data:
#     print(" ".join(server.data))
# else:
#     print("Пусто")


# task 7

# class Contact:
#     def __init__(self, name):
#         self.name = name
#         self.phone_numbers = []
#
#     def add_phone_numbers(self, *numbers):
#         self.phone_numbers.extend(numbers)
#
#     def display_phone_numbers(self):
#         if self.phone_numbers:
#             print(", ".join(self.phone_numbers))
#         else:
#             print("Не найдено")
#
#
# contacts = {}
#
# contact1 = Contact("Иван")
# contact2 = Contact("Мария")
#
# contact1.add_phone_numbers("123-456-789", "987-654-321")
# contact2.add_phone_numbers("111-222-333")
#
# contacts[contact1.name] = contact1
# contacts[contact2.name] = contact2
#
# requested_name = input("Введите имя контакта: ")
# if requested_name in contacts:
#     contacts[requested_name].display_phone_numbers()
# else:
#     print("Контакт не найден.")

