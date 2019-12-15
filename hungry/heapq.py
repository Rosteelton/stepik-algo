# Задача на программирование: очередь с приоритетами

# Первая операция добавляет число xx в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
# Sample Input:
#
# 6
# Insert 200
# Insert 10
# ExtractMax
# Insert 5
# Insert 500
# ExtractMax
# Sample Output:
#
# 200
# 500

import heapq

if __name__ == '__main__':

    heap = []

    count = int(input())
    for k in range(count):
        str = input().split()
        if str[0] == "Insert":
            number = int(str[1])
            heapq.heappush(heap, -number)
        else:
            print(-heapq.heappop(heap))
