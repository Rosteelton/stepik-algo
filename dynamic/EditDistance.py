# Задача на программирование: расстояние редактирования
# Вычислите расстояние редактирования двух данных непустых строк, содержащих строчные буквы латинского алфавита.

# Sample Input 2:
# short
# ports
# Sample Output 2:
# 3

def editDist(word1, word2):
    w, h = len(word1) + 1, len(word2) + 1
    matrix = [[0 for x in range(w)] for y in range(h)]

    for i in range(w):
        matrix[0][i] = i

    for j in range(h):
        matrix[j][0] = j

    for j in range(1, h):
        for i in range(1, w):
            insert = matrix[j][i - 1]
            delete = matrix[j - 1][i]
            match = matrix[j - 1][i - 1]

            if word1[i - 1] == word2[j - 1]:
                replace = 0
            else:
                replace = 1
            matrix[j][i] = min(insert + 1, delete + 1, match + replace)
    return matrix[h-1][w-1]



def main():
    word1 = input()
    word2 = input()
    result = editDist(word1, word2)
    print(result)

if __name__ == '__main__':
    main()