# python3
#### https://math.stackexchange.com/questions/442459/for-the-fibonacci-numbers-show-for-all-n-f-12f-22-dotsf-n2-f-nf-n1
i = int(input())
lesser_n = i%60
lesser_nplus = (i + 1)%60

def fibo(n):
    x, y = 0, 1
    for a in range(2, i + 1):
        z = x + y
        z = z % 10
        y, x = z, y
    return z

if lesser_n <= 1:
    x = lesser_n
else:
    x = fibo(lesser_n)
if lesser_nplus<=1:
    y = lesser_nplus
else:
    y = fibo(lesser_nplus)
    
print((x * y) % 10)
