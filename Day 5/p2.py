
## Advent of Code
## Day 5, Problem 2
## Dominic R. 2022

file = open('Day 5\input.txt', 'r')
lines = file.readlines()
file.close()

# function that reads commands passed in the 'move X from Y to Z' format
def readCommand(cmd_str):
    # move X from Y to Z
    command = cmd_str.split(' ')
    
    quantity = int(command[1])
    move_from = int(command[3]) - 1 # account for list numbering: [0-8] instead of [1-9]
    move_to = int(command[5]) - 1 # account for list numbering: [0-8] instead of [1-9]

    return [quantity, move_from, move_to]

# break apart the raw input and split it into a list representing the stacks
stacks = lines[0:8]
stack = [[]]
for row in stacks:
    new_row = row.replace(' ', '-').replace('[', '-').replace(']', '-').strip('-')
    for char in range(0, len(new_row), 4):
        stack[len(stack) - 1].append(new_row[char])
    stack.append([])
stack.pop()
# rotate the list clockwise by 90 degrees
new_stack = [list(r) for r in zip(*stack[::-1])]
for s in new_stack:
    while '-' in s:
        s.pop()

# interpret the commands
commands = lines[10:]
for c in commands:
    cmd = readCommand(c)
    # get the new slice (DON'T REVERSE)
    list_slice = ((new_stack[cmd[1]])[-cmd[0]:])
    # pop the slice out of the original list
    for i in range(0, cmd[0]):
        new_stack[cmd[1]].pop()
    # add the slice to the new stack
    new_stack[cmd[2]].extend(list_slice)

# get the code (lol easiest part)
code = ''
for n in new_stack:
    code += n[len(n) - 1]

print(code)