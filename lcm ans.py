# Python3

x, y = [int(i) for i in input().split()]

def gcd(x, y):
    if y == 0:
        return x
    z = x % y
    return gcd(y, z)
if x>y:
    ans = gcd(x, y)
else:
    ans = gcd(y, x)

print(x * y // ans)

