steps = 0
while True:
    line = input()
    if line == 'Going home':
        steps += int(input())
        break
    else:
        steps += int(line)

    if steps >= 10000:
        break

if steps < 10000:
    print(f'{1000 - steps} more steps to reach goal.')
else:
    print('Goal reached! Good job!')