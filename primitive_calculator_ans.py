# python3

import math

n = int(input())

# number of operations required for getting 0, 1, 2,.. , n
num_ops = [0, 0] + [math.inf]*(n-1)

for x in range(2, n+1):
    num1, num2, num3 = [math.inf]*3

    num1 = num_ops[x-1] + 1 
    if x%2 == 0: num2 = num_ops[x//2] + 1
    if x%3 == 0: num3 = num_ops[x//3] + 1
    min_ops = min(num1, num2, num3)
    num_ops[x] = min_ops

print(num_ops[n])

# Backtracking the numbers leading to n
nums = [n]
while n!=1:
    if n%3 ==0 and num_ops[n]-1 == num_ops[n//3]:
        nums += [n//3]
        n = n//3
    elif n%2 ==0 and num_ops[n]-1 == num_ops[n//2]:
        nums += [n//2]
        n = n//2
    else:
        nums += [n-1]
        n = n - 1

print(' '.join([str(i) for i in nums][::-1]))
