# Uses python3
import sys
import random

def partition3(a, l, r):
    pivot_value = a[l]
    p_l = i = l
    p_e = r
    while i <= p_e:
        if a[i] < pivot_value:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == pivot_value:
            i += 1
        else:
            a[i], a[p_e] = a[p_e], a[i]
            p_e -= 1
        pIndexes = [p_l, p_e]
    return pIndexes


def partition2(a, l, r):
    pivot = random.randint(l, r)
    a[r], a[pivot] = a[pivot], a[r]
    pivot_value = a[r]
    pIndex = l
    for i in range(l, r):
        if a[i] <= pivot_value:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex += 1
    a[r], a[pIndex] = a[pIndex], a[r]
    return pIndex


def randomized_quick_sort(a, l, r):
    if l >= r:
        return

    pivot = random.randint(l, r)
    a[l], a[pivot] = a[pivot], a[l]
    pIndex = partition3(a, l, r)
    randomized_quick_sort(a, l, pIndex[0] - 1)
    randomized_quick_sort(a, pIndex[1] + 1, r)

###############################################
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
