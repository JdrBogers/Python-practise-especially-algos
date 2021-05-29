# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):
    count = [0] * len(points)
    s_points = zip(starts, ['l'] * len(starts), range(len(starts)))
    e_points = zip(ends, ['r'] * len(ends), range(len(ends)))
    point_points = zip(points, ['p'] * len(points), range(len(points)))

    sort = chain(s_points, e_points, point_points)
    sort = sorted(sort, key=lambda a: (a[0], a[1]))
    segment = 0
    i = 0
    for num, letter, index in sort:
        if letter == 'l':
            segment += 1
        elif letter == 'r':
            segment -= 1
        else:
            count[index] = segment
            i += 1
    return count


def naive_count_segments(starts, ends, points):
    count = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                count[i] += 1
    return count

##########################################################
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
