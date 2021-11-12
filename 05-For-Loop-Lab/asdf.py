word = input()
sum = 0


for i in range(len(word)):
    sum += int(word[i])

print(f'The sum of the digits is:{sum}')