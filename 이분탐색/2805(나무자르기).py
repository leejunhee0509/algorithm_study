import sys
from math import inf
N,M = map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))
left = 0
right = max(tree)
answer = inf
while left<=right:
    mid = (left+right)//2
    sum = 0
    for item in tree:
        if item>=mid:
           sum+=(item-mid)
    if sum>=M:
        answer = mid
        left = mid+1
    else:
        right = mid-1
print(answer)