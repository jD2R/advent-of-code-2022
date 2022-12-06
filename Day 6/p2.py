with open('input.txt') as file:
    chars = [*file.readlines()[0]]
    for i in range(0, len(chars)-13):
        marker = chars[i:i+14]
        if all(j == 1 for j in [marker.count(c) for c in marker]):
            print(i + 14)
            break
