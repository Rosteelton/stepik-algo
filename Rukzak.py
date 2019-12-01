# Первая строка содержит количество предметов 1≤𝑛≤103 и вместимость рюкзака 0≤𝑊≤2⋅106.
# Каждая из следующих 𝑛 строк задаёт стоимость 0≤𝑐𝑖≤2⋅106 и объём 0<𝑤𝑖≤2⋅106 предмета (𝑛, 𝑊, 𝑐𝑖, 𝑤𝑖 — целые числа).
# Выведите максимальную стоимость частей предметов
# (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
# помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
#
# Sample Input:
#
# 3 50
# 60 20
# 100 50
# 120 30
# Sample Output:
#
# 180.000

result = 0

def findMaxCost(W, items):
    global result
    while W != 0 and items:
        item = items.pop(0)
        diff = W - item[1]
        if diff >= 0:
            result += item[0]
            return findMaxCost(diff, items)
        else:
            result += item[0] / item[1] * W
            return result
    return result

if __name__ == '__main__':

    items = []
    itemsNumber, W = map(int, input().split())
    for i in range(itemsNumber):
      x, y = map(int, input().split())
      items.append([x, y])

    items.sort(key= lambda x: x[0] / x[1], reverse=True)

    r = findMaxCost(W, items)
    print('{:.3f}'.format(r))
