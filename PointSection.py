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

def findPoints2(segments):
    dots = [segments.pop(0)[1]]
    for l, r in segments:
        if l > dots[-1]:
            dots.append(r)
    return dots

def contains(x, *tuple):
   return (x in range(tuple[0], tuple[1]))

if __name__ == '__main__':
    sections = []
    sectionCount = int(input())

    for i in range(sectionCount):
       x, y = map(int, input().split())
       sections.append([x, y])

    sections.sort(key= lambda x: x[1])

    dots = findPoints2(sections)

    print(len(dots))
    print(" ".join(map(str, dots)))


