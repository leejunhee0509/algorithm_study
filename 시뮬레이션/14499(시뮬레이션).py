import sys
from collections import deque
N,M,x,y,K = map(int,sys.stdin.readline().split())
ground = []
for _ in range(N):
    ground.append(list(map(int,sys.stdin.readline().split())))
op = list(map(int,sys.stdin.readline().split()))
dx = [0,0,0,-1,1] # 동1 서2 북3 남4
dy = [0,1,-1,0,0]
sx = deque() 
sy = deque()
sz = deque()

for i in range(4):
    sx.append(0)
    sy.append(0)

for i in range(len(op)):
    dir = op[i]
    nx = x+dx[dir]
    ny = y+dy[dir]
    if 0<=nx<N and 0<=ny<M:
        if dir==1:
            sx.rotate(1)  #양수 시계, 음수 반시계
            sy[0] = sx[0]
            sy[2] = sx[2]
        elif dir==2:
            sx.rotate(-1)
            sy[0] = sx[0]
            sy[2] = sx[2]
        elif dir == 3:
            sy.rotate(-1)
            sx[0] = sy[0]
            sx[2] = sy[2]
        else:
            sy.rotate(1)
            sx[0] = sy[0]
            sx[2] = sy[2]

        if ground[nx][ny]==0:
            ground[nx][ny] = sx[0]
        else:
            sx[0] = ground[nx][ny]
            sy[0] = ground[nx][ny]
            ground[nx][ny] = 0
        print(sx[2])
        x = nx
        y = ny
    
