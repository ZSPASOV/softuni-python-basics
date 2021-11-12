number = int(input())

total = 0
counter = 0
while counter < number:
    amount = float(input())
    counter += 1
    if amount < 0:
        print('Invalid operation!')
        break
    else:
        print(f'Increase: {amount:.2f}')
        total += amount


print(f'Total: {total:.2f}')