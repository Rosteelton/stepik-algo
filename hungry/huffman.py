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
    def __init__(self, freq, value = None, left_subtree = None, right_subtree = None):
        self.freq = freq
        self.value = value
        self._left_subtree = left_subtree
        self._right_subtree = right_subtree

    def __repr__(self):
        return 'Tree({0}, {1})'.format(self.value, self.freq)

# def createFreqSortedTree(list):
#     i = 0
#     treeList = map(lambda x: Tree(x(1), x(0)), list)
#     while treeList:
#         sorted(treeList, key = lambda leaf: leaf.freq)
#         a = treeList.pop(0)
#         treeList.-
#         Tree()


if __name__ == '__main__':
    string = input()

    result = createFrequencyMap(string)
    print(result.items())

    treeList = map(lambda x: Tree(x[1], x[0]), result.items())

    print(sorted(treeList, key = lambda leaf: leaf.freq))


