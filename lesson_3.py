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

