# Задача на программирование: различные слагаемые
# По данному числу 1≤𝑛≤109 найдите максимальное число 𝑘,
# для которого 𝑛 можно представить как сумму 𝑘 различных натуральных слагаемых.
# Выведите в первой строке число 𝑘, во второй — 𝑘 слагаемых.

# Sample Input 1:
#
# 4
# Sample Output 1:
#
# 2
# 1 3


if __name__ == '__main__':
    number = int(input())

    counter = 1
    result = []
    while number != 0:
        diff = number - counter
        if diff > counter or diff == 0:
            number -= counter
            result.append(counter)
            counter += 1
        else:
            counter += 1

    print(len(result))
    print(" ".join(map(str,result)))




