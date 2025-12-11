initialNumber = 1234355612312321

initialNumber = 221385913859

def checkEqualOrNot(initialNumber):
    # print("checkEqualOrNot was called with input " + str(initialNumber))
    lengthOfNumber = len(str(initialNumber))

    if lengthOfNumber <= 1:
        return

    midway = int(lengthOfNumber/2)

    leftNumber = int(str(initialNumber)[0:midway])
    rightNumber = int(str(initialNumber)[midway:lengthOfNumber])
    if leftNumber == rightNumber:
        print("Found repeating number: " + str(leftNumber))
        return leftNumber
    else:
        checkEqualOrNot(leftNumber)
        checkEqualOrNot(rightNumber)

# checkEqualOrNot(initialNumber)
lengthOfNumber = len(str(initialNumber))
counter = 0

while counter < lengthOfNumber:
    print(str(initialNumber)[counter:])
    partOfNumber = int(str(initialNumber)[counter:])
    counter += 1
    checkEqualOrNot(partOfNumber)