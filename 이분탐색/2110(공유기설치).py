import sys
from math import inf
N,C = map(int,sys.stdin.readline().split())
ground = []
for _ in range(N):
    ground.append(int(sys.stdin.readline()))
ground.sort()

left = 1
right = ground[-1]-left
answer = 0
while left<=right:
    cnt = 1
    prev = ground[0]
    mid = (left+right)//2
    tmp = inf
    for i in range(len(ground)):
        if ground[i] - prev >= mid:
            tmp = min(tmp, ground[i]-prev)
            prev = ground[i]
            cnt+=1
    if cnt>=C:
        left = mid+1
        answer = tmp
    else:
        right = mid-1
print(answer)
        
            