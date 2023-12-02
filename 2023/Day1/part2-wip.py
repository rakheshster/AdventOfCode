numberDictionary = {
    'one': '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

inputLines = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

for inputString in inputLines.splitlines():
    originalString = inputString
    for item in numberDictionary:
        inputString = inputString.replace(item,numberDictionary[item])
    print(originalString, '=>', inputString)


# === NEW ATTEMPT ===
numberDictionary = {
    'one': '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

#inputString = "eightwothree"
inputString = "twoeightwothree"

matchesDictionary = {}
for item in numberDictionary:
    if item in inputString:
        matchesDictionary[inputString.index(item)] = numberDictionary[item]
        print(numberDictionary[item], 'at', inputString.index(item))

numbersList = []
for item in sorted(matchesDictionary):
    numbersList.append(matchesDictionary[item])

number = int(numbersList[0] + numbersList[-1])
print(number)
