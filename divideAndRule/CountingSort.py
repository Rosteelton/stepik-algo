# Задача на программирование: сортировка подсчётом
#
#
# Первая строка содержит число n, вторая — n натуральных чисел, не превышающих 10.
# Выведите упорядоченную по неубыванию последовательность этих чисел.

# Sample Input:
#
# 5
# 2 3 9 2 9
# Sample Output:
#
# 2 2 3 9 9

def sort(arr):
    result = arr.copy()
    counts = [0] * 10
    for j in range(len(arr)):
        counts[arr[j] - 1] += 1
    i = 0
    for k in range(len(counts)):
        while counts[k] != 0:
            result[i] = k + 1
            i += 1
            counts[k] -= 1
    return result

if __name__ == '__main__':
  _ = input()
  arr = list(map(int, input().split(" ")))
  result = sort(arr)
  print(" ".join(map(str, result)))