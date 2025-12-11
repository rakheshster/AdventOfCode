inputLines = open('Day4/sample.txt','r')
p1, isP1, grid = 0, True, [list("R" + line.strip() + "R") for line in inputLines]

print("GRID: "+str(grid))
border = list("." * len(grid[0]))
#print("BORDER: "+str(border))
#print("BORDER2: "+str([border]))
grid = [border] + grid + [border]
#print("GRID2: "+str(grid))

def isAccessible(i, j):
    cnt, neighbors = 0, [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j + 1], [i + 1, j - 1], [i + 1, j],
                         [i + 1, j + 1]]
    for k in neighbors:
        if grid[k[0]][k[1]] == "@":
            cnt += 1
    return True if cnt < 4 else False


def execute(isP1, cnt=0, ppt=[]):
    while True:
        ppt = [[i, j] for i, row in enumerate(grid) for j, v in enumerate(row) if v == "@" and isAccessible(i, j)]
        cnt += len(ppt)
        if not ppt: return cnt
        for i, j in ppt: grid[i][j] = "."; ppt = []
        if isP1: return cnt


print("Part1:", (p1 := execute(isP1=True, cnt=0)))
print("Part2:", execute(isP1=False, cnt=p1))