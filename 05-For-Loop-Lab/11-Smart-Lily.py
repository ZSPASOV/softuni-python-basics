age = int(input())
machine_price = float(input())
price_per_toy = int(input())

savings = 0
toys_counter = 0

#to age + 1, because in python the right interval is the number you input - 1
#so if we want to check for 10 years it will get value 10 + 1 = 11, but it will be
#read as 10
for i in range (1, age + 1):
    if i % 2 == 0:
        savings += i * 5 #since she gets 5 leva per year
        savings -= 1 #since the brother takes 1 lev for each year
    else:
        toys_counter += 1

total_toys_price = price_per_toy * toys_counter
savings += total_toys_price

if savings >= machine_price:
    money_left = savings - machine_price
    print(f'Yes! {money_left:.2f}')
else:
    needed_money = machine_price - savings
    print(f'No! {needed_money:.2f}')

