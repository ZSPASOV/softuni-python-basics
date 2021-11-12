even_numbers_1 = [i for i in range(-2, 10, 3) if i % 2 == 0]

even_numbers_2 = []
for i in range(10):
    if i % 2 == 0:
        even_numbers_2.append(i)

print(even_numbers_1)
print(even_numbers_2)



