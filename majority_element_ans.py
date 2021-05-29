# Uses python3
import sys

def get_majority_element(a, l, r):
    if l == r:
        return -1
    if l + 1 == r:
        return a[l]

    l_elem = get_majority_element(a, l, (l + r - 1) // 2 + 1)
    r_elem = get_majority_element(a, (l + r - 1) // 2 + 1, r)

    lcount = 0
    for i in range(l, r):
        if a[i] == l_elem:
            lcount += 1
    if lcount > (r - l) // 2:
        return l_elem

    rcount = 0
    for i in range(l, r):
        if a[i] == r_elem:
            rcount += 1
    if rcount > (r - l) // 2:
        return r_elem

    return -1

#####################################################
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
