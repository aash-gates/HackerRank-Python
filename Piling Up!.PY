from collections import deque 
import sys
for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    for i in arr:
        assert i&lt;=2**31 - 1
    lst = deque(arr)

    curr = 9999999999999999
    flag = 0
    if (len(lst)0):
        flag = 0
        if (left >= right and left  left and right 0 or latest > curr:
        print "No"
    else:
        print "Yes"