is_even_counter = 0
for i in range(5):
    number = int(input())
    if number % 2 == 0:
        is_even_counter += 1

print(f'percentage even numbers: {is_even_counter / 5 * 100} %')

