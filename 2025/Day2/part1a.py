#initialNumber = 1234355612312321

#initialNumber = 138591385911
initialNumber = "38593859"

def checkEqualOrNot(initialNumber):
    #print("checkEqualOrNot was called with input " + str(initialNumber))
    lengthOfNumber = len(str(initialNumber))

    if lengthOfNumber <= 1:
        return 0

    midway = int(lengthOfNumber/2)

    leftNumber = int(str(initialNumber)[0:midway])
    rightNumber = int(str(initialNumber)[midway:lengthOfNumber])
    if leftNumber == rightNumber:
        # print("Found repeating number: " + str(leftNumber) + str(rightNumber))
        return int(str(leftNumber) + str(rightNumber))
    else:
        checkEqualOrNot(leftNumber)
        checkEqualOrNot(rightNumber)
        return 0

def goThroughDigitsAndReturnEquals(initialNumber):
    lengthOfNumber = len(str(initialNumber))
    listOfRepeatingNumbers = []

    counter = 0
    while counter < lengthOfNumber:
        #print(str(initialNumber)[counter:])
        partOfNumber = int(str(initialNumber)[counter:])
        counter += 1
        output = checkEqualOrNot(partOfNumber)
        if output > 0: 
            listOfRepeatingNumbers.append(output)


    counter = 0
    while counter < lengthOfNumber - 1:
        #print(str(initialNumber)[:-1 - counter])
        partOfNumber = int(str(initialNumber)[:-1 - counter])
        counter += 1
        output = checkEqualOrNot(partOfNumber)
        if output > 0: 
            listOfRepeatingNumbers.append(output)

    if len(listOfRepeatingNumbers) > 0:
        return max(listOfRepeatingNumbers)
    else:
        return 0


# print(goThroughDigitsAndReturnEquals(initialNumber))


ourInput="38593856-38593862"
startingNumber = int(ourInput.split("-")[0])
endingNumber = int(ourInput.split("-")[1])

for i in range(startingNumber, endingNumber + 1):
    #print(str(i))
    output = goThroughDigitsAndReturnEquals(str(i))
    if output > 0:
        print("Repeating number is: " + str(output))
