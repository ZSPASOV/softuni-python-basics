import sys
number_inputs = int(input())
counter = 0
max_number = -sys.maxsize
while counter < number_inputs:
    counter += 1
    number_typed = int(input())
    if number_typed > max_number:
        max_number = number_typed
print(max_number)
