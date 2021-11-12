sum = 0

while True:
    command = input()
    if command =='Stop':
        break
    number = int(command)
    sum += number
print(sum)