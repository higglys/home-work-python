triangles = [
[3, 4, 5],
[1, 2, 2],
[6, 8, 10],
[5, 5, 5],
[7, 10, 12],
[4, 5, 6],
[2, 3, 4],
[8, 15, 17],
[9, 9, 12],
[10, 11, 13]
]


def square(a, b, c):
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    return s

largest = triangles[0]
max_square = square(largest[0], largest[1], largest[2])

for triangle in triangles:
    s = square(triangle[0], triangle[1], triangle[2])

    if s > max_square:
        max_square = s
        largest = triangle

    area = max_square ** 0.5

print("Самый большой треугольник:", largest)
print("Его площадь:", area)




