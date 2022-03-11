import sys
from collections import deque
from math import inf
N = int(input())
ground = []
for _ in range(N):
    ground.append(list(map(int,sys.stdin.readline().split())))
dx = [-1,1,0,0]
dy = [0,0,1,-1]   
answer = inf
temp = 2
def init(i,j):
    global temp
    q = deque()
    visit = [[-1]*N for _ in range(N)]
    visit[i][j] = 0
    ground[i][j] = temp
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and ground[nx][ny] ==1:
                if visit[nx][ny] == -1:
                    visit[nx][ny] = 0
                    ground[nx][ny] = temp
                    q.append((nx,ny))
for i in range(N):
    for j in range(N):
        if ground[i][j] == 1:
            init(i,j)
            temp+=1

def bfs(i,j,check):
    global answer
    visit = [[0]*N for _ in range(N)]
    visit[i][j] = 0
    q = deque()
    q.append((i,j,check))
    while q:
        x,y,color = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if ground[nx][ny]==0 and visit[nx][ny] ==0:
                    visit[nx][ny] = visit[x][y]+1
                    q.append((nx,ny,color))
                elif ground[nx][ny]!=0 and ground[nx][ny]!=color:
                    return(visit[x][y])
    return inf

for i in range(N):
    for j in range(N):
        if ground[i][j] != 0:
            temp = bfs(i,j,ground[i][j])
            answer= min(temp, answer)
print(answer)
    