#note - in nested loops it is important to break the two loops if you seek a certain break criteria

start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
counter = 0
combination_found = False
for i in range (start_interval,end_interval+1):
    for j in range (start_interval,end_interval+1):
        sum = i + j
        counter +=1
        if sum == magic_number:
            combination_found = True
            break
    if combination_found == True:
        break
if combination_found == True:
    print(f'Combination N:{counter} ({i} + {j} = {magic_number})')
else:
    print(f'{counter} combinations - neither equals {magic_number}')
