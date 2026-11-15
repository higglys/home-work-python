def average_marks(students):                            # 8 задание
    result = {}

    for student, marks in students.items():
        if marks:
            result[student] = sum(marks) / len(marks)
        else:
            result[student] = 0

    return result



students = {
    "Анна": [5, 4, 5],
    "Иван": [3, 4],
    "Олег": []
}

print(average_marks(students))




def group_by_mark(students):                        #9 задание
    result = {}

    for student, mark in students.items():
        if mark not in result:
            result[mark] = []

        result[mark].append(student)

    return result



students = {
    "Аня": 5,
    "Игорь": 4,
    "Лена": 5
}

print(group_by_mark(students))




def word_statistics(words):                             # 10 задание
    frequencies = {}


    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1


    most_popular = None
    max_count = 0

    for word in words:
        if frequencies[word] > max_count:
            max_count = frequencies[word]
            most_popular = word

    return frequencies, most_popular



words = ["кот", "пёс", "кот", "лиса", "пёс", "кот"]

print(word_statistics(words))