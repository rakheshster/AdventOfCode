numberList = ['1','2','3','4','5','6','7','8','9']

inputLines = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".splitlines()

# Comment this out when testing, so I use the test text from above
inputLines = open('./input-rak.txt','r')

# to capture the sum of all the numbers
runningTotal = 0

for inputString in inputLines:
    # don't do anything for empty lines
    if len(inputString) == 0:
        continue

    # capture the original string so I can output it later; 
    # remove any newlines so the output looks good
    originalString = inputString.strip()

    matchingNumbers = []

    for character in inputString:
        if character in numberList:
            matchingNumbers.append(character)

    number = int(matchingNumbers[0] + matchingNumbers[-1])
    runningTotal += number

    print(originalString, '=>', number)

print('The total is', str(runningTotal))