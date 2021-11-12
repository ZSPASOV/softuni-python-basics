floors = int(input())
rooms = int(input())
output = ''
for f in range (floors, 0, -1):
    for r in range(rooms):
        #last floor:
        if f == floors:
            output += f'L{f}{r} '
        elif f % 2 == 0:
            output += f'O{f}{r} '
        else:
            output += f'A{f}{r} '
    output+= '\n'

print(output)