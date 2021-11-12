sum = 0
command = input()
while command != 'Stop':
    number = int(command)
    sum += number
    command = input()
print(sum)