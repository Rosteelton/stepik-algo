result = []

def findPoints(sections):
    if not sections:
        return result
    else:
        newSections = []
        point = sections[0][1]
        result.append(point)
        for item in sections:
            if not contains(point, item[0], item[1] + 1):
                newSections.append(item)
        return findPoints(newSections)

def contains(x, *tuple):
   return (x in range(tuple[0], tuple[1]))

if __name__ == '__main__':
    sections = []
    sectionCount = int(input())

    for i in range(sectionCount):
       x, y = map(int, input().split())
       sections.append([x, y])

    sections.sort(key= lambda x: x[1])

    findPoints(sections)

    print(len(result))
    print(" ".join(map(str, result)))


