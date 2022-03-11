import sys

N,M = map(int,sys.stdin.readline().split())
time = []
for _ in range(N):
    time.append(int(sys.stdin.readline()))
time.sort()
left = 0
right = M*time[-1]

while left<=right:
    mid = (left+right)//2
    people = 0
    for i in range(N):
        people += mid//time[i]
    if people>=M:
        answer = mid
        right = mid-1
    else:
        left = mid+1
print(answer)
    