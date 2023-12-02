numberDictionary = {
    'one': '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
    '1' : '1',
    '2' : '2',
    '3' : '3',
    '4' : '4',
    '5' : '5',
    '6' : '6',
    '7' : '7',
    '8' : '8',
    '9' : '9',
}

inputLines = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
five4sevenfourtwonvnldmvpeightfive
""".splitlines()

# Comment this out when testing, so I use the test text from above
inputLines = open('./input-rak.txt','r')

# to capture the sum of all the numbers
runningTotal = 0

# process each line; uncomment one of these depending on whether I am ready from the file or testing
for inputString in inputLines:
    # don't do anything for empty lines
    if len(inputString) == 0:
        continue

    # capture the original string so I can output it later; 
    # remove any newlines so the output looks good
    originalString = inputString.strip()

    # a dictionary of all the numbers in the string
    # the keys are the position, values are the numbers
    # this way I can sort them at the end to get the correct order in which the numbers appeared! :)
    matchesDictionary = {}
    for item in numberDictionary:
        # only if the number text appears do I find the index & add it to the dictionary
        if item in inputString:
            # more than 1 match?
            if inputString.count(item) > 1:
                for counter in range(len(inputString) - 1):
                    if inputString.startswith(item,counter):
                        matchesDictionary[counter] = numberDictionary[item]
            else:
                matchesDictionary[inputString.index(item)] = numberDictionary[item]
            # print(numberDictionary[item], 'at', inputString.index(item))

    # an array that contains the numbers matched above, but sorted in the correct order
    numbersList = []
    for item in sorted(matchesDictionary):
        numbersList.append(matchesDictionary[item])

    # take the first and last numbers from the array, concatenate them and convert to an integer
    number = int(numbersList[0] + numbersList[-1])
    print(originalString, '=>', number)
    runningTotal += number

print('The total is', str(runningTotal))