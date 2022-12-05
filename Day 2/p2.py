
## Advent of Code
## Day 2, Problem 2
## Dominic R. 2022

## FILE HANDLING
# open the file in reading mode
file = open('Day 2\input.txt', 'r')
# grab the lines
lines = file.readlines()
# close the file
file.close()

# updated function that finds the amount of points you earn
def findPoints(elf, you):
    yourScore = 0
    
    match elf:
        # rock
        case "A":
            match you:
                case "X":
                    # loss, scissors
                    yourScore += 3
                case "Y":
                    # draw, rock
                    yourScore += 4
                case "Z":
                    # win, paper
                    yourScore += 8
        # paper
        case "B":
            match you:
                case "X":
                    # loss, rock
                    yourScore += 1
                case "Y":
                    # draw, paper
                    yourScore += 5
                case "Z":
                    # win, scissors
                    yourScore += 9
        # scissors
        case "C":
            match you:
                case "X":
                    # loss, paper
                    yourScore += 2
                case "Y":
                    # draw, scissors
                    yourScore += 6
                case "Z":
                    # win, rock
                    yourScore += 7

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
