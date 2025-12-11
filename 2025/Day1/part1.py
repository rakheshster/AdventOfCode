import sys

print(sys.argv)
startingNumber = sys.argv[1]
command = sys.argv[2]

print("I start with " + startingNumber + " and I must do command " + command)

inputLines = open('./input.txt','r')

for inputString in inputLines:
    # don't do anything for empty lines
    if len(inputString) == 0:
        continue

    # capture the original string so I can output it later; 
    # remove any newlines so the output looks good
    originalString = inputString.strip()

