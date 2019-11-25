from rcviz import CallGraph, viz
from functools import lru_cache

cg = CallGraph(filename="8.pdf")
dict = {}


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

def badFib(n):
    return n if n <= 1 else badFib(n-1) + badFib(n-2)

def badFibDict(n):
    if n not in dict:
        dict[n] = n if n <= 1 else badFibDict(n-1) + badFibDict(n-2)
    return dict[n]

def decCache(f):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner

if __name__ == "__main__":
    n = int(input())
    badFib2 = badFib

    badFib = lru_cache(maxsize=None)(badFib)
    print(badFib(n))

    badFib2 = decCache(badFib2)
    print(badFib2(n))




    # result2 = decCache(badFib)
    # print(result2(n))
