# task 1
print(17/2*3+2, 2+17/2*3, 19%4+15/2*3, 15+6-10*4, 17/2%2*3**3)

# task 2
print((17/2)*(3+2), (2+17)/2*3, 19%(4+15)/2*3, (15+(6-10))*4, 17/2%(2*3**3))

# task 3
Total_money = 11
Bread_cost = 1.5
amount_of_bread = 3
print(Total_money-Bread_cost * amount_of_bread)

# task 4
Anni_apples = 2
Pol_apples = 5
print(Pol_apples, Anni_apples)

# task 5
days = 5
print(days, "суток =", days * 24, "часов =", days * 24 * 60, "минут =", days * 24 * 60 * 60, "секунд")

# task 6
Days_in_a_week = 7
Days_have_passed = 182
print(Days_have_passed // Days_in_a_week)

# task 7
a = 150
b = 65
square_side = 30
print((a // square_side) * (b // square_side))

# task 8
seconds = 4000

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60
print(hours, "час")
print(minutes, "минут")
print(seconds, "секунд")


# task 9
cash = 361
denominations_1 = 100
denominations_2 = 50
denominations_3 = 10
denominations_4 = 1
number_of_denominations_1 = cash // denominations_1
number_of_denominations_2 = (cash % denominations_1) // denominations_2
number_of_denominations_3 = ((cash % denominations_1) % denominations_2) // denominations_3
number_of_denominations_4 = (((cash % denominations_1) % denominations_2) % denominations_3)

print(number_of_denominations_1, "купюры по", denominations_1, "рублей")
print(number_of_denominations_2, "купюры по", denominations_2, "рублей")
print(number_of_denominations_3, "купюры по", denominations_3, "рублей")
print(number_of_denominations_4, "купюры по", denominations_4, "рублей")