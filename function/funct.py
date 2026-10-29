def count_vowels(text):                             # Задача № 3 дз (function)
    vowels = "аеёиоуыэюя"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def positives(values):                             # Задача № 4 дз (function)
    result = []
    for num in values:
        if num > 0:
            result.append(num)
    return result

print(count_vowels('Программирование'))         # print № 3
print(positives([-2, 5, 0, 7, -1]))             # print № 4