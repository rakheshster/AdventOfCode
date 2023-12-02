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

# the maximum we have of each color
maxNumbers = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

# to capture the sum of all the numbers
runningTotal = 0

for inputString in inputLines:
    # don't do anything for empty lines
    if len(inputString) == 0:
        continue

    # split it along the game sets
    # first extract the game id - for this we split by : and take the first entry
    gameSetSnippet = inputString.split(':')[0]
    # what remains are all the sets, which we can split next
    setSnippet = inputString.split(':')[1]

    # replace 'Game ' from this to get the number :)
    gameNumber = int(gameSetSnippet.replace('Game ',''))

    # a variable to define if one of the sets below is invalid or not
    invalidSet = False

    # now process the sets
    for gameSet in setSnippet.split(';'):
        # this will give entries like:
        #  1 green, 1 blue, 1 red
        #  1 green, 8 red, 7 blue
        #  6 blue, 10 red
        #  4 red, 9 blue, 2 green

        # only proceed is we haven't identified a set to be invalid
        if invalidSet == True:
            continue

        for setColour in gameSet.replace(' ','').split(','):
            # the above will split a line into array elements like: ['1green', '1blue', '1red']
            for colour in maxNumbers:
                if colour in setColour and int(setColour.replace(colour, '')) > maxNumbers[colour]:
                    #print("Flagging colour",colour,"in",gameSet.lstrip())
                    invalidSet = True

    if invalidSet == False:
        print("Game",str(gameNumber),"is valid")
        runningTotal += gameNumber
    else:
        print("Game",str(gameNumber),"is invalid =>",inputString)

print(runningTotal)