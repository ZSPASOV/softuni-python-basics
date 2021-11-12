length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage_used_volume = float(input())
volume = (length_cm * width_cm * height_cm) * 0.001
volume_water = (volume * (100 - percentage_used_volume)) / 100
print(f'{volume_water:.3f}')