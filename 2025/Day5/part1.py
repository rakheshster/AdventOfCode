inputLines = open('Day5/inputRak.txt','r')

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
    #print(item)

    for item2 in listOfFreshIngredients:
        startingRange = int(item2.split('-')[0])
        endingRange = int(item2.split('-')[1])

        if int(item) > startingRange and int(item) < endingRange:
            print(".")
            counter += 1

print(counter)