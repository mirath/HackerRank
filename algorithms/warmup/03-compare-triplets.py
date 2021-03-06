#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    pa = 0
    pb = 0

    pa += (a0 > b0)
    pa += (a1 > b1)
    pa += (a2 > b2)

    pb += (a0 < b0)
    pb += (a1 < b1)
    pb += (a2 < b2)

    return [pa, pb]

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
