inputLines = open('sample2.txt','r')

listOfFreshIngredients = []
listOfAvailableIngredients = []

inSecondHalf = False

for line in inputLines:
    if inSecondHalf == False and line.strip() != '':
        listOfFreshIngredients.append(line.strip())

    if line.strip() == '':
        inSecondHalf = True

    if inSecondHalf == True and line.strip() != '':
        listOfAvailableIngredients.append(line.strip())

#print(listOfFreshIngredients)
#print(listOfAvailableIngredients)

allFreshIngredients = []

counter = 0
for item in listOfAvailableIngredients:
    itemIsFresh = False
    #print(item)

    for item2 in listOfFreshIngredients:
        if itemIsFresh:
            break

        startingRange = int(item2.split('-')[0])
        endingRange = int(item2.split('-')[1])

        if int(item) > startingRange and int(item) < endingRange:
            itemIsFresh = True
            counter += 1

# print("part 1: " + str(counter))

# part 2
tempList = []

for item2 in listOfFreshIngredients:
    startingRange = int(item2.split('-')[0])
    endingRange = int(item2.split('-')[1])

    tempList.append((startingRange, endingRange))
    
    '''
    # this hangs for some reason.. memory
    for i in range(startingRange, endingRange + 1):
        if tempList.count(i) == 0:
            tempList.append(i)
    '''

print(tempList)
tempList = sorted(tempList)
print(tempList)

'''
The easiest way to cater for overlapping intervals was, for each new interval, 
subtract any other interval already processed from it before adding the resulting 
sub-intervals to the list of intervals. 
'''

'''
tempList2 = []
currentStart, currentEnd = tempList[0]

for start, end in tempList[1:]:
    print(start,end)
    if currentStart <= currentEnd + 1:
        # overlaps
        currentEnd = max(currentEnd, end)
    else:
        tempList2.append((currentStart, currentEnd))
        currentStart, currentEnd = start, end

tempList2.append((currentStart, currentEnd))

print(tempList2)
'''


# print("part 2: " + str(len(sorted(tempList))))

# the problem is the overlapping ranges...