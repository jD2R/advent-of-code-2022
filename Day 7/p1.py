# Couldn't figure it out, so I availed myself of the community.
# Enormous amount of the structure and theory provided by CyberAstronaut101's solution.
#  - https://github.com/CyberAstronaut101/advent-of-code/blob/main/2022/22_d7.py

with open('input.txt') as file:
    def parse_input(input):
        file_system = {}
        curr_dir = ""

        for i, command in enumerate(input):
            command = command.split()
            if command[0] == '$':
                if command[1] == "cd":
                    if command[2] == "/":
                        # move to root dir
                        curr_dir = ""
                    elif command[2] == "..":
                        # move up a directory
                        curr_dir = "/".join(curr_dir.split('/')[:-1])
                    else:
                        # move to sub directory
                        curr_dir += "/" + command[2]
                    continue
                elif command[1] == "ls":
                    continue
            # If the line was not a command, we can get the file size
            # First modify the dict used to track the filesystem state
            working_dir = get_dir(file_system, curr_dir)
            if command[0] == "dir":
                if command[1] not in working_dir:
                    working_dir[command[1]] = dict()
                continue
            working_dir[command[1]] = int(command[0])

        return file_system

    def get_dir(fs, dir):
        result = fs

        for d in dir.split("/"):
            if d == "":
                continue
            result = result[d]

        return result

    def calculate_dir_sizes(fs, name):
        sizes = []
        size = 0
        for key in fs.keys():
            if type(fs[key]) is dict:
                res = calculate_dir_sizes(fs[key], key)
                size += res[-1][1]
                sizes.extend(res)
            else:
                size += fs[key]

        sizes.append([name, size])
        return sizes

    file_system = parse_input(file.readlines())
    all_dir_sizes = calculate_dir_sizes(file_system, "/")

    total_size = 0
    for dir in all_dir_sizes:
        if dir[1] <= 100000:
            total_size += dir[1]

    print(total_size)

