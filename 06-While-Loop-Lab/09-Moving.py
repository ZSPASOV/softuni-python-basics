width = int(input())
length = int(input())
height = int(input())
command = input()
has_volume = True
volume_of_one_box = 1
room_volume = width * length * height

while command != 'Done':
    number_boxes = int(command)
    room_volume -= number_boxes * volume_of_one_box
    if room_volume < 0:
        has_volume = False
        break
    command = input()
if has_volume == True:
    print(f'{room_volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(room_volume)} Cubic meters more.')