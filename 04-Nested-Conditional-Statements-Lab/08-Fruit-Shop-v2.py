fruit = input()
day = input()
amount = float(input())
price = 0
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
fruits_prices_week = {'banana': 2.50, 'apple': 1.20, 'orange': 0.85, 'grapefruit': 1.45, 'kiwi': 2.70,
                      'pineapple': 5.50, 'grapes': 3.85}
fruits_prices_weekend = {'banana': 2.70, 'apple': 1.25, 'orange': 0.90, 'grapefruit': 1.60, 'kiwi': 3.00,
                         'pineapple': 5.60, 'grapes': 4.20}
if day not in(week + weekend) or fruit not in fruits_prices_week.keys() or fruit not in fruits_prices_weekend.keys():
    print('error')
elif day in week:
    final_price = amount * fruits_prices_week[fruit]
    print(f'{final_price:.2f}')
else:
    final_price = amount * fruits_prices_weekend[fruit]
    print(f'{final_price:.2f}')


