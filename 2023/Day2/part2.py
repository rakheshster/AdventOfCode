inputLines = """
Game 1: 1 green, 1 blue, 1 red; 1 green, 8 red, 7 blue; 6 blue, 10 red; 4 red, 9 blue, 2 green; 1 green, 3 blue; 4 red, 1 green, 10 blue
Game 2: 9 red, 7 green, 3 blue; 15 green, 2 blue, 5 red; 10 red, 3 blue, 13 green
Game 3: 3 red, 1 blue, 4 green; 6 red, 3 green, 2 blue; 6 red, 16 blue, 1 green
Game 4: 2 blue, 2 green, 19 red; 3 blue, 11 red, 16 green; 18 blue, 13 green, 20 red; 18 red, 12 blue, 16 green; 8 green, 16 blue, 16 red
Game 5: 8 green, 1 red, 12 blue; 10 green, 6 red, 13 blue; 1 red, 3 blue, 6 green; 14 blue, 2 red, 7 green
Game 6: 1 red; 1 blue; 2 green, 1 blue; 1 red, 3 blue; 1 red, 2 blue, 2 green; 1 green, 7 blue, 1 red
""".splitlines()

# Comment this out when testing, so I use the test text from above
inputLines = open('./input-rak.txt','r')

# to capture the sum of all the powers
runningTotal = 0

for inputString in inputLines:
    # don't do anything for empty lines
    if len(inputString) == 0:
        continue

    # split it along the game sets
    # first remove the "Game :" but so we get the snippet with the sets
    setSnippet = inputString.split(':')[1]

    minColours = {
        'green' : 0,
        'blue' : 0,
        'red' : 0
    }

    # process the sets
    for gameSet in setSnippet.split(';'):
        # this will give entries like:
        #  1 green, 1 blue, 1 red
        #  1 green, 8 red, 7 blue
        #  6 blue, 10 red
        #  4 red, 9 blue, 2 green

        for setColour in gameSet.replace(' ','').split(','):
            # the above will split a line into array elements like: ['1green', '1blue', '1red']
            for colour in minColours:
                if colour in setColour and int(setColour.replace(colour, '')) > minColours[colour]:
                    minColours[colour] = int(setColour.replace(colour, ''))

    # now find the power
    power = 1
    print(inputString.rstrip())
    for colour in minColours:
        print("\tMinimum",colour,"is",minColours[colour],"")
        power = power * minColours[colour]

    print()
    runningTotal += power

print("Total POWER is",str(runningTotal))