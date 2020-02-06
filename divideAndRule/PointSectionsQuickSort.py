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
import random

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
    m1 = partition_1(arr, l, r, random.randint(l, r), extracter)
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

def contains(x, *tuple):
   return (x in range(tuple[0], tuple[1]))



def find(points, sections):
 # ???


def main():
    n, _ = map(int, input().split(" "))
    sections = []
    for _ in range(n):
        x, y = map(int, input().split(" "))
        sections.append((x, y))
    points = list(map(int, input().split(" ")))

    quicksort(points, lambda x: x)
    print(points)

    quicksort(sections, lambda x: x[1])
    print(sections)


if __name__ == '__main__':
    main()
