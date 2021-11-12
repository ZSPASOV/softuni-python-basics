product = input()
city = input()
amount = float(input())
price_a = 0
if city == 'Sofia':
    if product == 'coffee':
        price_a = 0.50
        price = price_a * amount
        print(price)
    elif product == 'water':
        price_a = 0.80
        price = price_a * amount
        print(price)
    elif product == 'beer':
        price_a = 1.20
        price = price_a * amount
        print(price)
    elif product == 'sweets':
        price_a = 1.45
        price = price_a * amount
        print(price)
    elif product == 'peanuts':
        price_a = 1.60
        price = price_a * amount
        print(price)
elif city == 'Plovdiv':
    if product == 'coffee':
        price_a = 0.40
        price = price_a * amount
        print(price)
    elif product == 'water':
        price_a = 0.70
        price = price_a * amount
        print(price)
    elif product == 'beer':
        price_a = 1.15
        price = price_a * amount
        print(price)
    elif product == 'sweets':
        price_a = 1.30
        price = price_a * amount
        print(price)
    elif product == 'peanuts':
        price_a = 1.50
        price = price_a * amount
        print(price)
elif city == 'Varna':
    if product == 'coffee':
        price_a = 0.45
        price = price_a * amount
        print(price)
    elif product == 'water':
        price_a = 0.70
        price = price_a * amount
        print(price)
    elif product == 'beer':
        price_a = 1.10
        price = price_a * amount
        print(price)
    elif product == 'sweets':
        price_a = 1.35
        price = price_a * amount
        print(price)
    elif product == 'peanuts':
        price_a = 1.55
        price = price_a * amount
        print(price)