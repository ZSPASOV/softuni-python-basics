floors = int(input())
rooms = int(input())

for f in range (floors, 0, -1):
    for r in range(rooms):
        #last floor:
        if f == floors:
            print(f'L{f}{r}', end = ' ') #end prints them on same row with space
        elif f % 2 == 0:
            print(f'O{f}{r}', end = ' ')
        else:
            print(f'A{f}{r}', end=' ')
    print() # this will print each new value of f with the corresponding r on a new row