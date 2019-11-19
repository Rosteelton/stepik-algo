def fib(n):
    qwerty = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 2
    while i != n:
        qwerty.append((qwerty[i - 1] + qwerty[i - 2]))
        i = i + 1
    return qwerty[n-1] + qwerty[n-2]

def fib2(n):
    prev, cur = 0, 1

    for i in range(1, n):
        prev, cur = cur, prev + cur

    return cur

def fibLastNumber(n):
    prev, cur = 0, 1

    for i in range(1, n):
        sum1 = prev + cur
        prev = cur
        if sum1 > 9:
            cur = sum1 % 10
        else:
            cur = sum1
    return cur


def main():
    n = int(input())
    print(fibLastNumber(n))


if __name__ == "__main__":
    main()