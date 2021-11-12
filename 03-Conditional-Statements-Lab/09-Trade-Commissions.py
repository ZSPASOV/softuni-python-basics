city = input()
sales_amount = float(input())
if city == 'Sofia':
    if 0 <= sales_amount <= 500:
        bonus = sales_amount * 0.05
        print(f'{bonus:.2f}')
    elif 500 < sales_amount <= 1000:
        bonus = sales_amount * 0.07
        print(f'{bonus:.2f}')
    elif 1000 < sales_amount <= 10000:
        bonus = sales_amount * 0.08
        print(f'{bonus:.2f}')
    elif sales_amount > 10000:
        bonus = sales_amount * 0.12
        print(f'{bonus:.2f}')
    else:
        print('error')
elif city == 'Varna':
    if 0 <= sales_amount <= 500:
        bonus = sales_amount * 0.045
        print(f'{bonus:.2f}')
    elif 500 < sales_amount <= 1000:
        bonus = sales_amount * 0.075
        print(f'{bonus:.2f}')
    elif 1000 < sales_amount <= 10000:
        bonus = sales_amount * 0.10
        print(f'{bonus:.2f}')
    elif sales_amount > 10000:
        bonus = sales_amount * 0.13
        print(f'{bonus:.2f}')
    else:
        print('error')
elif city == 'Plovdiv':
    if 0 <= sales_amount <= 500:
        bonus = sales_amount * 0.055
        print(f'{bonus:.2f}')
    elif 500 < sales_amount <= 1000:
        bonus = sales_amount * 0.08
        print(f'{bonus:.2f}')
    elif 1000 < sales_amount <= 10000:
        bonus = sales_amount * 0.12
        print(f'{bonus:.2f}')
    elif sales_amount > 10000:
        bonus = sales_amount * 0.145
        print(f'{bonus:.2f}')
    else:
        print('error')
else:
    print('error')

