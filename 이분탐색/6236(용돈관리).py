import sys

N,M = map(int,sys.stdin.readline().split())

money = []
for _ in range(N):
    money.append(int(sys.stdin.readline()))

left = min(money)
right = sum(money)
answer = 1000000
while left<=right:
    mid = (left + right)//2
    now = 0
    cnt = 0
    if mid<max(money):
        left = mid+1
    else:
        for i in range(N):
            if now<money[i]:
                now = mid
                cnt+=1
            now -=money[i]
        if cnt>M:
            left = mid+1
        else:
            answer = mid
            right = mid-1

print(answer)