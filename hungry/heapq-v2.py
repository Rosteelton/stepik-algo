import math
import sys


def getParentIndex(i):
    return math.floor((i + 1) / 2) - 1


def getLeftChildIndex(i):
    return (i + 1) * 2 - 1


def getRightChildIndex(i):
    return (i + 1) * 2


def getValueIfExists(list, index):
    try:
        return list[index]
    except IndexError:
        return sys.maxsize


def shiftup(list):
    currentIndex = len(list) - 1
    parentIndex = getParentIndex(currentIndex)
    while parentIndex >= 0 and list[parentIndex] > list[currentIndex]:
        list[currentIndex], list[parentIndex] = list[parentIndex], list[currentIndex]
        currentIndex, parentIndex = parentIndex, getParentIndex(parentIndex)
    return list


def shiftdown(list):
    currentIndex = 0
    length = len(list)
    child1Index = getLeftChildIndex(currentIndex)
    child2Index = getRightChildIndex(currentIndex)

    while child1Index < length:
        if list[currentIndex] > min(list[child1Index], getValueIfExists(list, child2Index)):
            if list[child1Index] < getValueIfExists(list, child2Index):
                list[child1Index], list[currentIndex] = list[currentIndex], list[child1Index]
                currentIndex = child1Index
                child1Index = getLeftChildIndex(currentIndex)
                child2Index = getRightChildIndex(currentIndex)
            else:
                list[child2Index], list[currentIndex] = list[currentIndex], list[child2Index]
                currentIndex = child2Index
                child1Index = getLeftChildIndex(currentIndex)
                child2Index = getRightChildIndex(currentIndex)
        else:
            break
    return list


def heappush(list, number):
    list.append(number)
    return shiftup(list)


def heappop(list):
    result = list[0]
    list[0] = list[len(list) - 1]
    del list[-1]
    return (shiftdown(list), result)


def test():
    a = [4, 18, 7, 20, 21, 18, 42, 53, 22, 23]
    assert (shiftup(a) == a)
    b = [4, 18, 7, 20, 21, 18, 42, 53, 22, 1]
    br = [1, 4, 7, 20, 18, 18, 42, 53, 22, 21]
    assert (shiftup(b) == br)
    c = [4, 18, 7, 20, 21, 18, 42, 53, 22]
    assert (heappush(c, 1) == br)
    d = [1]
    assert (heappush(d, 0) == [0, 1])
    d = []
    assert (heappush(d, 0) == [0])
    e = [1, 0, 2]
    assert (shiftdown(e) == [0, 1, 2])
    f = [8, 18, 7, 20, 21, 18, 42, 53, 22, 23]
    assert (shiftdown(f) == [7, 18, 8, 20, 21, 18, 42, 53, 22, 23])
    g = [53, 18, 7, 20, 21, 18, 42, 53, 22, 23]
    assert (shiftdown(g) == [7, 18, 18, 20, 21, 53, 42, 53, 22, 23])
    h = [2, 3, 15]
    assert(heappush(heappush(h, 18), 12) == [2, 3, 15, 18, 12])
    i = [2, 3, 15, 18, 12]
    assert heappop(i) == ([3, 12, 15, 18], 2)
    j = [3, 12, 15, 18]
    assert heappop(j) == ([12, 18, 15], 3)

def main():
    heap = []

    count = int(input())
    for k in range(count):
        str = input().split()
        if str[0] == "Insert":
            number = int(str[1])
            heappush(heap, -number)
        else:
            heap, value = heappop(heap)
            print(-value)

if __name__ == '__main__':
    main()
