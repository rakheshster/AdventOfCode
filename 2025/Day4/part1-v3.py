# This is mine and Akku version
inputLines = open('Day4/sample.txt','r')
grid = [list("R" + line.strip() + "R") for line in inputLines]

lengthOfList = len(grid[0])
boundaryList = [list("R" * lengthOfList)]

gridWithBoundary = boundaryList + grid + boundaryList

print(gridWithBoundary)

def getAllNeighbours(theGrid, x, y):
    neighbourIndexes = [
        [x, y + 1],
        [x, y - 1],
        [x + 1, y],
        [x + 1, y + 1],
        [x + 1, y - 1],
        [x - 1, y - 1],
        [x - 1, y ],
        [x - 1, y + 1]
    ]

    listofNeighbours = []

    for index1, index2 in neighbourIndexes:
        theLetter = theGrid[index1][index2]
        if theLetter != "R":
            listofNeighbours.append(theLetter)

    return listofNeighbours


lengthOfGridWithBoundary = lengthOfList
depthOfGridWithBoundary = len(gridWithBoundary)

# print(lengthOfGridWithBoundary, depthOfGridWithBoundary)

accessibleCounter = 0
rowCounter = 1
while rowCounter < lengthOfGridWithBoundary - 1:
    #print(gridWithBoundary[rowCounter])

    columnCounter = 1
    while columnCounter < lengthOfGridWithBoundary - 1:
        # print(str(rowCounter) + "," + str(columnCounter) + " | " + str(gridWithBoundary[rowCounter][columnCounter]))

        if gridWithBoundary[rowCounter][columnCounter] == "@":
            myNeighbours = getAllNeighbours(gridWithBoundary, rowCounter, columnCounter)

            if myNeighbours.count("@") < 4:
                print(str(rowCounter) + "," + str(columnCounter))
                accessibleCounter += 1

        columnCounter += 1

    rowCounter += 1

print(accessibleCounter)

'''
rowCounter = 1
for outerList in gridWithBoundary:
    columnCounter = 1
    for innerList in outerList:
        print(str(rowCounter) + "," + str(columnCounter) + " | " + str(innerList))

        #print("My neighbors are: ")
        #getAllNeighbours(gridWithBoundary, rowCounter, columnCounter)
        #print("===")

        columnCounter += 1

    rowCounter += 1
'''

'''
rowNum = 0
for gridLine in gridWithBoundary:
    columnNum = 0
    for eachElement in gridLine:
        print(str(rowNum) + str(columnNum) + str(eachElement))
        columnNum += 1
    rowNum += 1
'''

'''
for index1, index2 in gridWithBoundary:
    print(gridWithBoundary)


print(getAllNeighbours(gridWithBoundary, 1, 3))
'''

# print(str(grid[0][1]))
