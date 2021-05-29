# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    max = 0
    lindex = list()
    index = 0
    
    while capacity > 0:
        max = 0
        for i in range(len(weights)):
            if values[i]/weights[i]>=max and not(i in lindex):
                max = values[i]/weights[i]
                index = i

        x = min(weights[index],capacity)
        capacity -= x
        value += x * max
        lindex.append(index)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
