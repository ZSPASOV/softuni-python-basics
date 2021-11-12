days_spent = int(input())
room_type = input()
evaluation = input()

if room_type == 'room for one person':
    if evaluation == 'positive':
        fee = (18.00 * (days_spent - 1)) + (18.00 * (days_spent - 1) * 0.25)
        print(f'{fee:.2f}')
    elif evaluation == 'negative':
        fee = (18.00 * (days_spent - 1)) - (18.00 * (days_spent - 1) * 0.10)
        print(f'{fee:.2f}')
elif room_type == 'apartment':
    if days_spent < 10 and evaluation == 'positive':
        fee = (25.00 * (days_spent - 1) * 0.70) + (25.00 * (days_spent - 1) * 0.70 * 0.25)
        print(f'{fee:.2f}')
    elif days_spent < 10 and evaluation == 'negative':
        fee = (25.00 * (days_spent - 1) * 0.70) - (25.00 * (days_spent - 1) * 0.70 * 0.10)
        print(f'{fee:.2f}')
    elif 10 <= days_spent <= 15 and evaluation == 'positive':
        fee = (25.00 * (days_spent - 1) * 0.65) + (25.00 * (days_spent - 1) * 0.65 * 0.25)
        print(f'{fee:.2f}')
    elif 10 <= days_spent <= 15 and evaluation == 'negative':
        fee = (25.00 * (days_spent - 1) * 0.65) - (25.00 * (days_spent - 1) * 0.65 * 0.10)
        print(f'{fee:.2f}')
    elif days_spent > 15 and evaluation == 'positive':
        fee = (25.00 * (days_spent - 1) * 0.50) + (25.00 * (days_spent - 1) * 0.50 * 0.25)
        print(f'{fee:.2f}')
    elif days_spent > 15 and evaluation == 'negative':
        fee = (25.00 * (days_spent - 1) * 0.50) - (25.00 * (days_spent - 1) * 0.50 * 0.10)
        print(f'{fee:.2f}')
elif room_type == 'president apartment':
    if days_spent < 10 and evaluation == 'positive':
        fee = (35.00 * (days_spent - 1) * 0.90) + (35.00 * (days_spent - 1) * 0.90 * 0.25)
        print(f'{fee:.2f}')
    elif days_spent < 10 and evaluation == 'negative':
        fee = (35.00 * (days_spent - 1) * 0.90) - (35.00 * (days_spent - 1) * 0.90 * 0.10)
        print(f'{fee:.2f}')
    elif 10 <= days_spent <= 15 and evaluation == 'positive':
        fee = (35.00 * (days_spent - 1) * 0.85) + (35.00 * (days_spent - 1) * 0.85 * 0.25)
        print(f'{fee:.2f}')
    elif 10 <= days_spent <= 15 and evaluation == 'negative':
        fee = (35.00 * (days_spent - 1) * 0.85) - (35.00 * (days_spent - 1) * 0.85 * 0.10)
        print(f'{fee:.2f}')
    elif days_spent > 15 and evaluation == 'positive':
        fee = (35.00 * (days_spent - 1) * 0.80) + (35.00 * (days_spent - 1) * 0.80 * 0.25)
        print(f'{fee:.2f}')
    elif days_spent > 15 and evaluation == 'negative':
        fee = (35.00 * (days_spent - 1) * 0.80) - (35.00 * (days_spent - 1) * 0.80 * 0.10)
        print(f'{fee:.2f}')

