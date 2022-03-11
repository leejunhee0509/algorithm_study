import sys
from collections import deque
from math import inf
M,N = map(int,sys.stdin.readline().split())
ground = []
point = []
for i in range(N):
    ground.append(list(sys.stdin.readline().strip()))
    for j in range(M):
        if ground[i][j] == 'C':
           point.append((i,j))
dx = [0,-1,0,1] #west north east south
dy = [-1,0,1,0]
visit = [[inf]*M for _ in range(N)]
def bfs(i,j):
    q = deque()
    for a in range(4):
        nx = i+dx[a]
        ny = j+dy[a]
        if 0<=nx<N and 0<=ny<M and ground[nx][ny] !='*':
            q.append((nx,ny,a))
            visit[nx][ny] = 0
    while q:
        x,y,cdir = q.popleft()
        for ndir in range(4):
            
            nx = x+dx[ndir]
            ny = y+dy[ndir]
            if 0<=nx<N and 0<=ny<M and ground[nx][ny] !='*':
                cnt = visit[x][y]
                if cdir==0 or cdir==2:
                    if ndir == 1 or ndir==3:
                        cnt+=1
                else:
                    if ndir==2 or ndir == 0:
                        cnt+=1
                        
                if visit[nx][ny] == inf:
                    visit[nx][ny] = cnt
                    q.append((nx,ny,ndir))
                else:
                    if visit[nx][ny]>cnt:
                        visit[nx][ny] =cnt
                        q.append((nx,ny,ndir))
    return
bfs(point[0][0], point[0][1])
print(visit[point[1][0]][point[1][1]])