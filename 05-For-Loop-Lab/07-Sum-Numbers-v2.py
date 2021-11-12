n = int(input())
sum = 0
for _ in range(n):  # _ here _ means no variable is assigned, we just need to repeat the operation n times
  number  = int(input())
  sum = sum + number
print(sum)

# note here we do not put start of the range, it will be just the value of n