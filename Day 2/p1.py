
## Advent of Code
## Day 2, Problem 1
## Dominic R. 2022

## FILE HANDLING
# open the file in reading mode
file = open('input.txt', 'r')
# grab the lines
lines = file.readlines()
# close the file
file.close()

# function that finds the amount of points you earn
def findPoints(elf, you):
    yourScore = 0
    
    match elf:
        # rock
        case "A":
            match you:
                # rock
                case "X":
                    yourScore += 4
                # paper
                case "Y":
                    yourScore += 8
                # scissors
                case "Z":
                    yourScore += 3
        # paper
        case "B":
            match you:
                # rock
                case "X":
                    yourScore += 1
                # paper
                case "Y":
                    yourScore += 5
                # scissors
                case "Z":
                    yourScore += 9
        # scissors
        case "C":
            match you:
                # rock
                case "X":
                    yourScore += 7
                # paper
                case "Y":
                    yourScore += 2
                # scissors
                case "Z":
                    yourScore += 6
                    
    # return the score
    return yourScore

# array of scores
scores = []
# iterate through each line
for line in lines:
    # line[0] = elf, line[2] = you
    scores.append(findPoints(line[0], line[2]))

# print the sum of the scores
print(sum(scores))
