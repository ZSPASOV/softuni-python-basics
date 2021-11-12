flag = False
condition = False
n = int(input())
for i in range(n):
    for j in range(n):
        if condition:
            flag = True
            break
    if flag:
        break

