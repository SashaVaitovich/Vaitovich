# task 1

# with open('text_file.txt') as file:
#     lines = file.readlines()
# for line in lines:
#     if line.rstrip().endswith('!'):
#         print(line.rstrip())


# task 2

# with open('input.txt', 'w') as input_file:
#     user_input = input("Введите 10 чисел через пробел: ")
#     input_file.write(user_input)
# with open('input.txt', 'r') as input_file:
#     numbers_str = input_file.read()
#     numbers_list = list(map(int, numbers_str.spit()))
# product = 1
# for num in numbers_list:
#     product *= num
# with open('output.txt', 'w') as output_file:
#     output_file.write(str(product))


# task 3
#
# from datetime import datetime, timedelta
#
#
# def parse_date(date_str):
#     return datetime.strptime(date_str.strip(), "%Y-%m-%d")
#
#
# def is_more_than_a_month(date):
#     return datetime.now() - date > timedelta(days=30)
#
#
# with open(file='product.txt', encoding="utf-8") as file:
#     lines = file.readlines()
#
# filtered_products = []
# for line in lines:
#     name, quantity, price, date_str = line.strip().split(',')
#     quantity = int(quantity)
#     price = int(price)
#     date = parse_date(date_str)
#
#     if is_more_than_a_month(date) and quantity * price > 1000000:
#         filtered_products.append({
#             "name": name,
#             "quantity": quantity,
#             "price": price,
#             "date": date
#         })
#
# for product in filtered_products:
#     print(f"Товар: {product['name']}, Количество: {product['quantity']}, "
#           f"Цена: {product['price']}, Дата поступления: {product['date']}")


# task 4

# import json
#
# dictionary = {
#     12345: ('Саша', 21),
#     23456: ('Паша', 22),
#     34567: ('Ксюша', 23),
#     45678: ('Даша', 24),
#     56789: ('Петя', 25)
# }
#
# with open('dictionary.json', 'w', encoding='utf-8') as file:
#     json.dump(dictionary, file, ensure_ascii=False)


# task 5

# import json
# import csv
#
# with open('dictionary.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#
# with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=';')
#
#     csv_writer.writerow(['person', 'name', 'age'])
#
#     for key, (name, age) in data.items():
#         csv_writer.writerow(['person', name, age])


# task 6

# try:
#     x = (1, 2, 5, 7)
#     x = x / 2
#     print(x)
# except TypeError:
#     print("TypeError:(")


# task 7

# try:
#     print(input("Введите один символ: ")[1])
# except IndexError:
#     print("IndexError :((")


# task 8

# try:
#     print(input("Введите любое значение: ") + int(input("Введите любое число: ")))
# except TypeError:
#     print("TypeError :(((")


# task 9
#
# try:
#     file = open("lesson_111.py")
#     file.write("srt")
#     file.close()
# except FileNotFoundError:
#     print("FileNotFoundError :((((")


# task 10

# def remove_element(my_list, element_to_remove):
#     if element_to_remove in my_list:
#         my_list.remove(element_to_remove)
#         print(f"Элемент {element_to_remove} успешно удален.")
#     else:
#         raise TypeError(f"Элемента {element_to_remove} нет в списке.")
#
#
# my_list = [1, 2, 3, 4, 5]
# element_to_remove = int(input("Введите элемент для удаления: "))
# remove_element(my_list, element_to_remove)
