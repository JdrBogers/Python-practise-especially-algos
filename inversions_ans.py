# Uses python3
import sys


def merge(a, b, l, ave, r):
    count = 0
    i, j, k = l, ave, l
    while i <= ave - 1 and j <= r:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
            count += ave - i
        k += 1
    while i <= ave - 1:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= r:
        b[k] = a[j]
        j += 1
        k += 1
    for i in range(l, r + 1):
        a[i] = b[i]
    return count

def merge_sort(a, b, l, r):
    count = 0
    if r > l:
        ave = (l + r) // 2
        count += merge_sort(a, b, l, ave)
        count += merge_sort(a, b, ave + 1, r)
        count += merge(a, b, l, ave + 1, r)
    return count

##################################################################
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(merge_sort(a, b, 0, len(a) - 1))
