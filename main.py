# 1 задание 123 123 123

def compressString(string):
    compressedString = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressedString += string[i - 1]
            if count > 1:
                compressedString += str(count)
            count = 1
    compressedString += string[-1]
    if count > 1:
        compressedString += str(count)
    return compressedString

s = input("Введите строку для преобразования: ")
compressedString = compressString(s)
print(compressedString)

# 2 задание

def decompressString(s):
    decompressed = ""
    count = ""
    for i in range(len(s)):
        if s[i].isdigit():
            count += s[i]
            count = int(count) - 1
            decompressed += s[i - 1] * int(count)
            count = ''
        else:
            decompressed += s[i]

    return decompressed

s = input("Введите строку для преобразования: ")
decompressedString = decompressString(s)
print(decompressedString)

# 3 задание

from collections import Counter

def mostCommonCharacters(s):
    s = s.replace(" ", "")
    count = Counter(s)
    mostCommon = count.most_common(3)
    for char, count in mostCommon:
        print(f"Символ '{char}' встречается {count} раз")

s = input("Введите строку: ")
mostCommonCharacters(s)

# 4 задание

def numberToText(number):
    ones = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    tens = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать',18: 'восемнадцать', 19: 'девятнадцать'}
    tensMultiple = {2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
    hundreds = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}
    if number == 0:
        return ones[0]
    elif number < 10:
        return ones[number]
    elif number < 20:
        return tens[number]
    elif number < 100:
        tensDigit = number // 10
        onesDigit = number % 10
        if onesDigit == 0:
            return tensMultiple[tensDigit]
        else:
            return tensMultiple[tensDigit] + " " + ones[onesDigit]
    elif number < 1000:
        hundredsDigit = number // 100
        remainingNumber = number % 100
        if remainingNumber == 0:
            return hundreds[hundredsDigit]
        else:
            return hundreds[hundredsDigit] + " " + numberToText(remainingNumber)
    else:
        return "Число должно быть в диапазоне от 1 до 1000"

n = int(input("Введите число от 1 до 1000: "))
textRepresentation = numberToText(n)
print(textRepresentation)
