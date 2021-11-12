import sys
number_inputs = int(input())
counter = 0
min_number = sys.maxsize
while counter < number_inputs:
    counter += 1
    number_typed = int(input())
    if number_typed < min_number:
        min_number = number_typed
print(min_number)
