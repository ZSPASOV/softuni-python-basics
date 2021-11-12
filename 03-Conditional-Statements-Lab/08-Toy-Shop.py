price_trip = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
sales_revenue = number_puzzles * 2.6 + number_dolls * 3 + number_bears * 4.1 + number_minions * 8.2 + number_trucks * 2
sold_toys = number_puzzles + number_dolls + number_bears + number_minions + number_trucks
if sold_toys >= 50:
    income = sales_revenue * 0.75 * 0.90
else:
    income = sales_revenue * 0.90
if income >= price_trip:
    money = income - price_trip
    print(f'Yes! {money:.2f} lv left.')
elif price_trip > income:
    money = price_trip - income
    print(f'Not enough money! {money:.2f} lv needed.')

