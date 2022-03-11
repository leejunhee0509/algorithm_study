import sys
from math import inf
N = int(input())
K = int(input())
#1~N,1~N, N제곱개
answer = 0
left=1
right = N*N
while left<=right:
    mid = (left+right)//2
    cnt=0
    for i in range(1,N+1):
        cnt+= min(mid//i,N)
    if cnt>=K:
        right = mid-1
        answer= mid
    else:
        left = mid+1
print(answer)