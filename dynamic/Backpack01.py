# Задача на программирование: рюкзак
# ﻿
#
# Первая строка входа содержит целые числа W и n — вместимость рюкзака и число золотых слитков.
# Следующая строка содержит n, задающих веса слитков. Н
# Найдите максимальный вес золота, который можно унести в рюкзаке.
#
# Sample Input:
#
# 10 3
# 1 4 8
# Sample Output:
#
# 9



def backPackBU(W, n, items):
    W += 1
    n += 1
    matrix = [[0 for x in range(W)] for y in range(n)]
    for i in range(1, n):
        for j in range(1, W):
            # используем тот же рюкзак без этого предмета
            matrix[i][j] = matrix[i-1][j]
            # если вес текущего предмета меньше текущего веса рюкзака
            currentItem = items[i-1]
            if currentItem <= j:
                matrix[i][j] = max(matrix[i][j], matrix[i-1][j-currentItem] + currentItem)
    return matrix[n-1][W-1]

def main():
    W, n = map(int, input().split(" "))
    items = list(map(int, input().split(" ")))

    result = backPackBU(W, n, items)
    print(result)

if __name__ == '__main__':
    main()