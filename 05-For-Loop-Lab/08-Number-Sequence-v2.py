import sys
n = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

#v paketa sys sys.maxsize e maximalnoto chislo v python
# za max_number slagame purvonachalna stoinost -sys.maxsize, koeto e nai otricatelnoto
# za min_number slagame parvonachalna stoinost sys.maxsize, koeto e max polojitelno