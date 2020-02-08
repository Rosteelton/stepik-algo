# Задача на программирование: точки и отрезки

# В первой строке задано два целых числа n  и m  — количество отрезков и точек на прямой, соответственно.
# Следующие nn строк содержат по два целых числа — координаты концов отрезков.
# Последняя строка содержит mm целых чисел — координаты точек.
# Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
# Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

# Sample Input:
#
# 2 3
# 0 5
# 7 10
# 1 6 11
# Sample Output:
#
# 1 0 0

# сортируем отрезки по началам (0), по концам (1)
# затем идем по точкам (x) и считаем сколько x >= в 1 группе и вычитаем из получившегося сколько x > во 2 группе
# юзать двоичный поиск!!! для нахождения (как bisect)

import random
import bisect

def partition_2(arr, l, r, reference, extracter):
    arr[l], arr[reference] = arr[reference], arr[l]
    x = arr[l]
    j = l
    for i in range(l + 1, r + 1):
        if extracter(arr[i]) < extracter(x):
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def partition_1(arr, l, r, reference, extracter):
    arr[l], arr[reference] = arr[reference], arr[l]
    x = arr[l]
    j = l
    for i in range(l + 1, r + 1):
        if extracter(arr[i]) <= extracter(x):
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def partition(arr, l, r, extracter):
    randomEl = random.choice([l, (l + r) // 2, r])

    m1 = partition_1(arr, l, r, randomEl, extracter)
    m0 = partition_2(arr, l, m1, m1, extracter)
    return m0, m1


def quicksort_(arr, l, r, extracter):
    if l >= r:
        return arr
    m0, m1 = partition(arr, l, r, extracter)
    quicksort_(arr, l, m0 - 1, extracter)
    quicksort_(arr, m1 + 1, r, extracter)


def quicksort(arr, extracter):
    quicksort_(arr, 0, len(arr) - 1, extracter)


# bad
def find(points, sectionsLeft, sectionsRight):
    dictionary = dict.fromkeys(points, 0)

    for point in points:

        j = 0
        while j < len(sectionsLeft) and point >= sectionsLeft[j][0]:
            j += 1

        k = 0
        while k < len(sectionsRight) and point > sectionsRight[k][1]:
            k += 1

        dictionary[point] = j - k

    return dictionary

def bisectFind(points, sectionsLeft, sectionsRight):
    for point in points:
        j = bisect.bisect_right(sectionsLeft, point)
        k = bisect.bisect_left(sectionsRight, point)
        print(j - k, end=' ')


def main():
    n, _ = map(int, input().split(" "))
    sections = []
    for _ in range(n):
        x, y = map(int, input().split(" "))
        sections.append((x, y))
    points = list(map(int, input().split(" ")))

    sectionsLeft = [i[0] for i in sections]
    sectionsRight = [i[1] for i in sections]

    quicksort(sectionsLeft, lambda x: x)
    quicksort(sectionsRight, lambda x: x)

    bisectFind(points, sectionsLeft, sectionsRight)

if __name__ == '__main__':
    main()
