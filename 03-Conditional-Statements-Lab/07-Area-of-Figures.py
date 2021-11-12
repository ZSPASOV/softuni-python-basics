import math

shape = input()
if shape == 'square':
    side_square = float(input())
    area = side_square * side_square
    print(f'{area:.3f}')
elif shape == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f'{area:.3f}')
elif shape == 'circle':
    r = float(input())
    area = r * r * math.pi
    print(f'{area:.3f}')
elif shape == 'triangle':
    base_b = float(input())
    height_b = float(input())
    area = (base_b * height_b) / 2
    print(f'{area:.3f}')

