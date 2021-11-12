n = int(input())
solutions = 0
for x1 in range (0, n + 1):
    for x2 in range (0, n + 1):
        for x3 in range (0, n + 1):
            if n == x1 + x2 + x3:
                solutions += 1
print(solutions)

