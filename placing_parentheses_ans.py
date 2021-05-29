# Uses python3
#import sys
import math
def evalt(a, b, op):
    """ Evaluates the expression (a op b)
    (int, int, char) -> (int) """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

###########################

def MinAndMax(n, m, i, j, x):
    min_val = math.inf
    max_val = -math.inf
    for k in range(i, j):
        a = evalt(n[i][k], n[k+1][j], x[k])
        b = evalt(n[i][k], m[k+1][j], x[k])
        c = evalt(m[i][k], n[k+1][j], x[k])
        d = evalt(m[i][k], m[k+1][j], x[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val


def get_maximum_value(q, x):
    l = len(q)
    m = [[None for x in range(l)] for x in range(l)]
    n = [[None for x in range(l)] for x in range(l)]
    for i in range(l):
        m[i][i] = q[i]
        n[i][i] = q[i]
    for s in range(1, l):
        for i in range(0, l-s):
            j = i + s
            m[i][j], n[i][j] = MinAndMax(n, m, i, j, x)
    return n[0][l-1]


if __name__ == "__main__":
    string = input()
    x, q = [], []

    for i in string:
        if i in ['+', '-', '*']:
            x.append(i)
        else:
            q.append(int(i))

    print(get_maximum_value(q, x))
