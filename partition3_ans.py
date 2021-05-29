# Uses python3
#import sys
#import itertools
import numpy

def partitions(weight, n, items):
    count = 0 
    val = numpy.zeros((weight+1, n+1))
    for i in range(1, weight+1):
        for j in range(1, n+1):
            val[i][j] = val[i][j-1]
            if items[j-1]<=i:
                temp = val[i-items[j-1]][j-1] + items[j-1]
                if temp > val[i][j]:
                    val[i][j] = temp
            if val[i][j] == weight: count += 1
    if count < 3: 
        print('0')
    else: 
        print('1')

if __name__ == '__main__':
    n = int(input())
    item_weights = [int(i) for i in input().split()]
    total_weight = sum(item_weights)
    if n<3: 
        print('0')
    elif total_weight %3 != 0: 
        print('0')
    else:
        partitions(total_weight // 3, n, item_weights)
