# Python3
# https://stackoverflow.com/questions/38950579/fibonacci-sum-of-large-numbersonly-last-digit-to-be-printed
i = int(input())

if i<=1:
    print(i)  
    quit()


last = (i+2)%60
if last==1:
    print(0)
    quit()
elif last==0:
    print(9)
    quit()
def fibo(i):
    x, y = 0, 1
    for n in range(2, last+1):
        z = x + y
        z = z%10
        y, x = z, y
    if z != 0:
        print(z - 1)
    else:
        print(9)
fibo(last)