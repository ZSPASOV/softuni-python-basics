movie_name = input()

standard_tickets_sold  = 0
student_tickets_sold  = 0
kids_tickets_sold  = 0
total_tickets_sold = 0


while movie_name != 'Finish':
    total_seats = int(input())
    free_seats = total_seats
    ticket_type = input()
    while free_seats > 0 and ticket_type != 'End':
        total_tickets_sold += 1
        free_seats -= 1

        if ticket_type == 'standard':
            standard_tickets_sold += 1
        elif ticket_type == 'kid':
            kids_tickets_sold += 1
        else:
            student_tickets_sold += 1

        if free_seats > 0:
            ticket_type = input()

    full_seats_percentage = 100 - (free_seats / total_seats * 100)
    print(f'{movie_name} - {full_seats_percentage:.2f}% full.')
    movie_name = input()

print(f'Total tickets: {total_tickets_sold}')

student_tickets_percentage = student_tickets_sold / total_tickets_sold * 100
standard_tickets_percentage = standard_tickets_sold / total_tickets_sold * 100
kids_tickets_percentage = kids_tickets_sold / total_tickets_sold * 100

print(f'{student_tickets_percentage:.2f}% student tickets.')
print(f'{standard_tickets_percentage:.2f}% standard tickets.')
print(f'{kids_tickets_percentage:.2f}% kids tickets.')