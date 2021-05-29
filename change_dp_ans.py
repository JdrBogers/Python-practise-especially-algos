# python3
import math

money = int(input())
denominations = [1, 3, 4]
min_coins = [0] + [math.inf] * money

for i in range(1, money+1):
    for j in denominations:
        if i >= j:
            coins = min_coins[i-j]+1
            if coins < min_coins[i]:
                min_coins[i] = coins

print(min_coins[money])