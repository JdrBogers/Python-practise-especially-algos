# Uses python3
import sys

def binary_search_iterative(a, x):
    l, r = 0, len(a) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

####################################################
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search_iterative(a, x), end=' ')
