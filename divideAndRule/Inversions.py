# Задача на программирование: число инверсий

# Первая строка содержит число n, вторая — массив, содержащий натуральные числа
#  . Необходимо посчитать число пар индексов 1 \le i \lt j \le n1≤i<j≤n, для которых A[i] \gt A[j]A[i]>A[j].
#  (Такая пара элементов называется инверсией массива.
#  Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
#  например, в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию,
#  инверсию образуют каждые два элемента.)

# Sample Input:
#
# 5
# 2 3 9 2 9
# Sample Output:
#
# 2
# MERGESORT algo


# need merge left part (l to m) and right (m + 1 to r)
def merge(arr, temp_arr, l, m, r):
    count = 0
    i = l  #left arr (to m)
    j = m + 1 #right arr (to r)
    k = i #temp arr

    print('merging {} with {}'.format(arr[l:m + 1], arr[m + 1: r + 1]))

    while i <= m and j <= r:
        if arr[i] <= arr[j]: # no inversions
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        else:
            count += m - i + 1
            temp_arr[k] = arr[j]
            j += 1
            k += 1

    while i <= m:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= r:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for s in range(l, r + 1):
        arr[s] = temp_arr[s]

    print('new arr = {}'.format(arr))
    print('count = {}', count)
    return count

# return number of inversions
def mergeSort(arr, temp_arr, l, r):
    count = 0
    if l < r:
        m = (l + r) // 2
        count += mergeSort(arr, temp_arr, l, m)
        count += mergeSort(arr, temp_arr, m + 1, r)
        count += merge(arr, temp_arr, l, m, r)
    return count


def find(array):
    temp_array = array.copy()
    return mergeSort(array, temp_array, 0, len(array) - 1)

def main():
    _ = int(input())
    array = list(map(int, input().split(" ")))
    result = find(array)
    print(result)

if __name__ == '__main__':
    main()
