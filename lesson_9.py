# task 1

# class Сalculation:

#     num_1 = 466
#     num_2 = 465
#
#     def num(self):
#         print(f'Число №1 {self.num_1}, число №2 {self.num_2}')
#
#     def change(self, new_num_1: int, new_num_2: int) -> tuple:
#         self.num_1 = new_num_1
#         self.num_2 = new_num_2
#         return new_num_1, new_num_2
#
#     def num_sum(self):
#         addition = self.num_1 + self.num_2
#         print(f'Сумма двух чисел равняется {addition}')
#
#     def equality(self):
#         if self.num_1 < self.num_2:
#             print(f'Число {self.num_2} больше {self.num_1}')
#         elif self.num_1 == self.num_2:
#             print(f'Число {self.num_1} равно числу {self.num_2}')
#         else:
#             print(f'Число {self.num_1} больше {self.num_2}')


# task 2

# class DecimalCounter:
#     def __init__(self, initial_value=0, min_value=0, max_value=100):
#         self._value = initial_value
#         self._min_value = min_value
#         self._max_value = max_value
#
#     @property
#     def value(self):
#         return self._value
#
#     def increment(self):
#         if self._value < self._max_value:
#             self._value += 1
#         else:
#             print('Достигнуто максимальное значение счетчика.')
#
#     def decrement(self):
#         if self._value > self._min_value:
#             self._value -= 1
#         else:
#             print('Достигнуто минимальное значение счетчика.')


# task 3

# class Shop:
#     def __init__(self, *products):
#         self.products = list(products)
#
#     def search(self, product):
#         if product in self.products:
#             print(f'Указанный товар есть в магазине')
#         else:
#             print(f'Указанный товар отсутствует в магазине')
#
#     def addition(self, new_product):
#         if new_product in self.products:
#             print(f'Данный товар уже есть в каталоге магазина')
#         else:
#             self.products.append(new_product)
#             print(f'Товар добавлен в каталог магазин')
#
#     def deletion(self, product):
#         if product in self.products:
#             self.products.remove(product)
#             print(f'Товар успешно удален')
#         else:
#             print(f'Товара с таким названием нету в каталоге магазина')


# task 4

# class MoneyBox:
#     def __init__(self, capacity: int) -> None:
#         self.capacity = capacity
#         self.coins = 0
#
#     def can_add(self, amount: int) -> bool:
#         return self.coins + amount <= self.capacity
#
#     def add(self, amount: int) -> None:
#         if self.can_add(amount):
#             self.coins += amount
#             print(f'Добавлено {amount} монет. Текущее количество монет: {self.coins}')
#         else:
#             print(f'Невозможно добавить {amount} монет. Превышена вместимость копилки.')
