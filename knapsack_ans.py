# python3
import numpy as np
import sys

def optimal_weight(W, w):
    mrx= np.zeros(shape=(len(w), W+1), dtype=int)
    for j in range(0, len(w)):
        for i in range(1, W+1):
            if w[j] > i:
                mrx[j, i] = mrx[j - 1, i]
            else:
                mrx[j, i] = max(w[j] + mrx[j - 1, i - w[j]], mrx[j - 1, i])
    return mrx[len(w) - 1, W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))