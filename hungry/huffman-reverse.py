# Задача на программирование: декодирование Хаффмана
#
# Восстановите строку по её коду и беспрефиксному коду символов.
#
# В первой строке входного файла заданы два целых числа kk и ll через пробел — количество различных букв,
# встречающихся в строке, и размер получившейся закодированной строки, соответственно.
# В следующих kk строках записаны коды букв в формате "letter: code". Ни один код не является префиксом другого.
# Буквы могут быть перечислены в любом порядке. В качестве букв могут встречаться лишь строчные буквы латинского алфавита;
# каждая из этих букв встречается в строке хотя бы один раз. Наконец, в последней строке записана закодированная строка.
# Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная строка имеет минимальный возможный размер.
#
#
# В первой строке выходного файла выведите строку ss. Она должна состоять из строчных букв латинского алфавита.
# Гарантируется, что длина правильного ответа не превосходит 10^4 символов.

# Sample Input 2:
#
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111
# Sample Output 2:
#
# abacabad


class SimpleTree(object):
    def __init__(self, value=None, rightSubTree=None, leftSubTree=None, parent=None):
        self.value = value
        self.rightSubTree = rightSubTree
        self.leftSubTree = leftSubTree
        self.parent = parent

    def __repr__(self):
        return "Tree({0}, left = {1}, right = {2})".format(self.value, self.leftSubTree, self.rightSubTree)

    def withLeftChild(self, leftSubTree):
        self.leftSubTree = leftSubTree

    def withRightChild(self, rightSubTree):
        self.rightSubTree = rightSubTree

    def assignValue(self, value):
        self.value = value

    def hasRightChild(self):
        return self.rightSubTree is not None

    def hasLeftChild(self):
        return self.leftSubTree is not None

    def hasParent(self):
        return self.parent is not None

    def getParent(self):
        return self.parent

    def isEmpty(self):
        return not self.hasRightChild() and not self.hasLeftChild()


def createChildOrGet(simpleTree, isRight):
    if isRight:
        if simpleTree.hasRightChild():
            return simpleTree.rightSubTree
        else:
            return SimpleTree(parent=simpleTree)
    else:
        if simpleTree.hasLeftChild():
            return simpleTree.leftSubTree
        else:
            return SimpleTree(parent=simpleTree)


def goToRoot(simpleTree):
    while simpleTree.hasParent():
        simpleTree = simpleTree.getParent()
    return simpleTree


def createTree(codes):
    currentTree = SimpleTree()

    for pair in codes:
        for char in pair[1]:
            if char == '0':
                child = createChildOrGet(currentTree, False)
                currentTree.withLeftChild(child)
                currentTree = child
            else:
                child = createChildOrGet(currentTree, True)
                currentTree.withRightChild(child)
                currentTree = child
        currentTree.assignValue(pair[0])
        currentTree = goToRoot(currentTree)
    return currentTree


def decode(simpleTree, bin):
    tempTree = simpleTree
    str = ""
    for b in bin:
        if b == '1':
            tempTree = tempTree.rightSubTree
            if tempTree.isEmpty():
                str += tempTree.value
                tempTree = tree
        else:
            tempTree = tempTree.leftSubTree
            if tempTree.isEmpty():
                str += tempTree.value
                tempTree = tree
    return str


if __name__ == '__main__':
    # part 2 reverse operation

    total, totalBits = map(int, input().split())

    codes = {}
    for k in range(total):
        sym, code = map(lambda a: a.strip(), input().split(":"))
        codes[sym] = code
    bits = input()

    listOfCodes = list(codes.items())  # [(a, 111), ...]

    tree = createTree(listOfCodes)
    decoded = decode(tree, bits)

    print(decoded)