# Задача на программирование: лестница
# Даны число n - ступенек лестницы и целые числа, которыми помечены ступеньки.
# Найдите максимальную сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до nn-й ступеньки),
# каждый раз поднимаясь на одну или две ступеньки.

# Sample Input 3:
#
# 3
# -1 2 1
# Sample Output 3:
#
# 3

# iterative
# все время интересует 2 предыдущих
def find3(arr):
    bb = 0
    before = arr[0]
    sum = before
    for i in range(1, len(arr)):
        current = arr[i]
        sum = max(bb + current, before + current)
        bb = before
        before = sum
    return sum

# noTailRec
def find2(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return max(arr[0], 0)
    else:
        return max(arr[-1] + find2(arr[:-1]), arr[-2] + find2(arr[:-2]))


# tailRec
def find1(arr, sum):
    if len(arr) == 0:
        return sum
    if len(arr) == 1:
        return max(sum + arr[0], sum)
    else:
        a = find1(arr[:-1], sum + arr[-1])
        b = find1(arr[:-2], sum + arr[-2])
        return max(a, b)


def test():
    assert(find2([2, -1]) + (-1) == 1)
    assert(find2([-1, -1]) + -1 == -2)
    assert(find2([-64, -16, -13, -9]) + -48 == -73)
    assert(find2([3, 4, 10, 10, 0, -6, -10]) + 0 == 21)

def main():

    _ = input()
    arr = list(map(int, input().split(" ")))

    # result = find1(arr[:-1], arr[-1])
    # result = arr[-1] + find2(arr[:-1])
    result = find3(arr)
    print(result)
    # test()
    # result = find3(arr)
    # print(result)

if __name__ == '__main__':
    main()