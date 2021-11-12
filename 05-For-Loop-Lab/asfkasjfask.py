num = input()
result = 0


for i in range(0, len(num), 1):
    n = int(num[i])
    result += n


print(f'The sum of the digits is:{result}')
