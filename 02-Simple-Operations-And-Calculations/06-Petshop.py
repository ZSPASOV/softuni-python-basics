number_dogs = int(input())
number_others = int(input())
dog_food = 2.5
other_food = 4
dogs_total_price = number_dogs * dog_food
number_others_total_price = number_others * other_food
total_sum = dogs_total_price + number_others_total_price
print(f'{total_sum:.2f} lv.')

