# Задача на программирование: калькулятор
# У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом xx:
# заменить xx на 2x2x, 3x3x или x+1x+1. По данному целому числу n определите минимальное число операций kk,
# необходимое, чтобы получить nn из 1. Выведите kk и последовательность промежуточных чисел.

# Sample Input 3:
#
# 96234
# Sample Output 3:
#
# 14
# 1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234

import queue

def solution(mins, n):
    q = queue.LifoQueue()
    fr = mins[n]
    value = n
    q.put(value)
    while fr != 1:
        n = fr
        fr = mins[n]
        value = n
        q.put(value)
    q.put(1)
    return q

def find(n):
    movements = [0, 0] + [n] * (n + 1)
    prevs = [0] * (n + 1)
    for i in range(1, n + 1):
        for k in (i * 2, i * 3, i + 1):
            if k <= n and movements[i] + 1 < movements[k]:
                movements[k] = movements[i] + 1
                prevs[k] = i
    return solution(prevs, n)

def main():
    n = int(input())

    if n==1:
        print(0)
        print(1)
    else:
        result = find(n)
        print(result.qsize()-1)
        while not result.empty():
            print(result.get(),end=" ")


if __name__ == '__main__':
    main()