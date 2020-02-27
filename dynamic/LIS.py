# Задача на программирование: наибольшая последовательнократная подпоследовательность
# Дано целое число n и массив A[1…n] натуральных чисел,
# Выведите максимальное k, для которого найдётся подпоследовательность,
# в которой каждый элемент делится на предыдущий

# Sample Input:
#
# 4
# 3 6 7 12
# Sample Output:
#
# 3

def lisBU(arr):
    counts = [1] * len(arr)

    for i, _ in enumerate(arr):
        for j in range(i):
            if arr[i] % arr[j] == 0 and counts[j] + 1 > counts[i]:
                counts[i] = counts[j] + 1
    return max(counts)

def main():
    _ = input()
    arr = list(map(int, input().split(" ")))
    result = lisBU(arr)
    print(result)

if __name__ == '__main__':
    main()