# task 1

string_value = "Строковое значение"

print(string_value[2])
print(string_value[-2])
print(string_value[:5])
print(string_value[:-2])
print(string_value[2::2])
print(string_value[1::2])
print(string_value[::-1])
print(string_value[::-2])
print(len(string_value))


# task 2

word = "Слово"
symbols_comparisonrison = word[0] == word[-1]
print(symbols_comparisonrison)


# task 3

word = "Слово"
print(word[1:4])
# или?
print(word[1], word[2], word[3])

# task 4

apple = "яблоко"
print(apple[1:-1] + " " + apple[3:])

# task 5

name = "Ivanou Ivan"
words = name.split()
reversed_sentence = ' '.join(reversed(words))
print(reversed_sentence)

# task 6

word = ("шалаш")
print(word == word[::-1])

# task 7

colors = ["red", "blue", "pink", "yellow", "black", "green"]
print(colors[1])

# task 8

line_1 = "employ"
line_2 = "employment"
print(line_1 in line_2)

# task 9

championship = "FIFA 2023"
first_F_index = championship.find("F")
second_F_index = championship.find("F", first_F_index + 1)

print(second_F_index)


# task 10

school = {"1a": 11, "1б": 16, "1в": 15, "1г": 12, "1д": 14, "2a": 9, "2б": 10, "2в": 15, "2г": 17, "2д": 8}

# а) в одном из классов изменилось количество учащихся.
school["1б"] = 22

# б) в школе появился новый класс.
school["1е"] = 9

# в) в школе был расформирован (удален) другой класс.
del school["1a"]

# г) Вычислите общее количество учащихся 9 классов в школе.
total_9th_grade = sum(list(school.values())[:9])
print(total_9th_grade)


