with open('input.txt') as file:
    chars = [*file.readlines()[0]]
    for i in range(0, len(chars)-3):
        marker = chars[i:i+4]
        if all(j == 1 for j in [marker.count(c) for c in marker]):
            print(i + 4)
            break
