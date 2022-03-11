import sys

M,N,L = map(int,sys.stdin.readline().split())
point = list(map(int,sys.stdin.readline().split()))
point.sort()
animal = []
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    animal.append((a,b))

cnt = 0
for x,y in animal:
    start = 0
    end = len(point)-1
    answer= -1
    while start<=end:
        mid = (start+end)//2
        if point[mid]<x:
            start = mid+1
        else:
            answer = mid
            end = mid-1
    if abs(point[answer]-x) +y <=L or abs(point[answer-1]-x)+y<=L:
        cnt+=1
print(cnt)