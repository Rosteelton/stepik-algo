# Задача на программирование: двоичный поиск
# ﻿
#
# Sample Input:
#
# 5 1 5 8 12 13
# 5 8 1 23 1 11
# Sample Output:
#
# 3 1 -1 1 -1


import math
import random


def findIndex(sortedList, number):
    l = 0
    r = len(sortedList) - 1

    while l <= r:
        middleIndex = math.floor((l + r) / 2)
        if sortedList[middleIndex] == number:
            return middleIndex
        elif number > sortedList[middleIndex]:
            l = middleIndex + 1
        else:
            r = middleIndex - 1
    return -2

def main():
    n1, *list1 = list(map(int, input().split()))
    n2, *list2 = list(map(int, input().split()))

    result = list(map(lambda x: findIndex(list1, x) + 1, list2))
    print(" ".join(map(str, result)))


def test(n_iter=100):
    for i in range(n_iter):
        l = random.randint(1, 100)
        k = random.randint(1, 100)

        list1 = []
        for _ in range(l):
            list1.append(random.randint(1, 10000))
        list1.sort()

        for _ in range(k):
            number = random.randint(1, 10000)
            findIndex(list1, number)


if __name__ == '__main__':
    main()
