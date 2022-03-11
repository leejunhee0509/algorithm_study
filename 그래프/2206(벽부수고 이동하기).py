import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
visit = [[[-1]*2 for _ in range(M)] for _ in range(N)]
ground = []
for _ in range(N):
    ground.append(list(map(int,sys.stdin.readline().strip())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs():
    q = deque()
    q.append((0,0,1))
    visit[0][0][1] = 1
    while q:
        x,y,life = q.popleft()
        if x==N-1 and y==M-1:
            return visit[x][y][life]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if ground[nx][ny] == 1 and life == 1:
                    if visit[nx][ny][life-1] == -1:
                        visit[nx][ny][life-1] = visit[x][y][life]+1
                        q.append((nx,ny,life-1))
                elif ground[nx][ny]==0 :
                    if visit[nx][ny][life] == -1:
                        visit[nx][ny][life] = visit[x][y][life]+1
                        q.append((nx,ny,life))
    return -1
    
print(bfs())