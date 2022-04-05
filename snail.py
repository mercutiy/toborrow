from math import ceil, log10
import sys
from typing import List


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isnumeric() or int(sys.argv[1]) < 1:
        usage = """
Usage: python3 snail.py <rank>

rank\tRank of the result matrix: positive integer value"""
        print(usage)
    else:    
        print(get_snail(int(sys.argv[1])))    

def get_snail_matrix(dim: int) -> List[List[int]]:
    if dim < 0:
        raise Exception('Dim cannot be negative')
    res = [[-1] * dim for _ in range(dim)]
    deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))
    delta = 0
    x, y = 0, 0
    next_node = lambda: (x + deltas[delta][0], y + deltas[delta][1])
    for i in range(dim ** 2):
        res[x][y] = i
        new_x, new_y = next_node()
        if new_x < dim and new_y < dim and res[new_x][new_y] == -1:
            # keep the track if next node is a valid one
            x, y = new_x, new_y
        else:
            # otherwise change the the direction
            delta = (delta + 1) % 4
            x, y = next_node()
    return res

def get_snail(dim: int) -> str:
    matrix = get_snail_matrix(dim)
    # Figure out about leading zeroes counts
    template = '{{:0{}d}}'.format(ceil(log10(dim ** 2)))
    return "\n".join(
        (' '.join(map(template.format, row)) for row in matrix)
    )

if __name__ == '__main__':
    main()
