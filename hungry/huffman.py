# Задача на программирование: кодирование Хаффмана
#
#
# По данной непустой строке ss длины не более 10^410
# 4
#  , состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код.
#  В первой строке выведите количество различных букв kk, встречающихся в строке,
#  и размер получившейся закодированной строки. В следующих kk строках запишите коды букв в
#  формате "letter: code". В последней строке выведите закодированную строку.

# Sample Input 2:
#
# abacabad
#
# Sample Output 2:
#
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111


# map (symbol, f - frequency)
def createFrequencyMap(str):
    map = {}
    for s in str:
        if s in map:
            map[s] = map[s] + 1
        else:
            map[s] = 1
    return map


class Tree(object):
    def __init__(self, freq, left_values=None, right_values=None, value=None, left_subtree=None, right_subtree=None):
        if right_values is None:
            right_values = set()
        if left_values is None:
            left_values = set()
        self.freq = freq
        self.value = value
        self.left_subtree = left_subtree
        self.right_subtree = right_subtree
        self.left_values = left_values
        self.right_values = right_values

    def isNotEmpty(self):
        return self.right_subtree is not None and self.left_subtree is not None

    def isEmpty(self):
        return self.right_subtree is None and self.left_subtree is None

    def __repr__(self):
        return 'Tree({0}, {1}, left = ${2}, right = ${3})'.format(self.value, self.freq, self.left_subtree,
                                                                  self.right_subtree)

def xset(s):
    if s is None:
        return []
    return set(s)


def createFreqSortedTree(source):
    treeList = list(map(lambda a: Tree(a[1], value=a[0]), source))
    while len(treeList) > 1:
        treeList.sort(key=lambda leaf: leaf.freq)
        a = treeList.pop(0)
        b = treeList.pop(0)
        treeList.append(Tree(a.freq + b.freq, left_subtree=a, right_subtree=b,
                             left_values=xset(a.left_values).union(xset(a.right_values)).union(xset(a.value)),
                             right_values=xset(b.left_values).union(xset(b.right_values)).union(xset(b.value))))
    return treeList[0]


def getSymbolCode(tree, symbol):
    code = ""
    while tree.isNotEmpty():
        if symbol in tree.right_values:
            tree = tree.right_subtree
            code = code + '1'
        elif symbol in tree.left_values:
            tree = tree.left_subtree
            code = code + '0'
    return code


def encode(tree, str):
    result = ""
    for s in str:
        result += getSymbolCode(tree, s)
    return result


def decode(tree, bin):
    tempTree = tree
    str = ""
    for b in bin:
        if b == '1':
            tempTree = tempTree.right_subtree
            if tempTree.isEmpty():
                str += tempTree.value
                tempTree = tree
        else:
            tempTree = tempTree.left_subtree
            if tempTree.isEmpty():
                str += tempTree.value
                tempTree = tree
    return str

if __name__ == '__main__':
    string = input()
    freqMap = createFrequencyMap(string)
    l = list(freqMap.items())
    # [('q', 2), ('w', 2), ('e', 1), ('r', 1), ('t', 1), ('y', 1)]
    resultTree = createFreqSortedTree(l)

    encoded = encode(resultTree, string)
    decoded = decode(resultTree, encoded)

    print(encoded)
    print(decoded)