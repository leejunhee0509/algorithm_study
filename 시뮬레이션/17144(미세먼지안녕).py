import sys
import copy

R,C,T = map(int,sys.stdin.readline().split())
ground = []
air = []
for i in range(R):
    ground.append(list(map(int,sys.stdin.readline().split())))
    for j in range(C):
        if ground[i][j] == -1:
            air.append((i,j))

def spread(ground):
    temp = copy.deepcopy(ground)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    d1x = [1,0,-1,0]
    d1y = [0,1,0,-1]
    for i in range(R):
        for j in range(C):
            if ground[i][j]!=-1 and ground[i][j]!=0:
                cnt = 0
                amount = ground[i][j]
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<R and 0<=ny<C and ground[nx][ny]!=-1:
                        cnt+=1
                        temp[nx][ny]+= amount//5
                temp[i][j] -= (amount//5)*cnt
    s1x = air[0][0]
    s1y = air[0][1]
    s2x = air[1][0]
    s2y = air[1][1]
    dir1 = 0
    dir2 = 0
    if s1x==0:
        for i in range(C-1,1,-1):
            temp[0][i] = temp[0][i-1]
        temp[0][1] = 0
    else:
        x = s1x+dx[dir1]
        y = s1y+dy[dir1]
        while(1):
            nx = x+dx[dir1]
            ny = y+dy[dir1]
            if nx==s1x and ny==s1y:
                temp[x][y] = 0
                break
            if 0<=nx<=s1x and 0<=ny<C:
                temp[x][y] = temp[nx][ny]
                x = nx
                y = ny
            else:
                dir1 = (dir1+1)%4
    if s2x == R-1:
        for i in range(C-1,1,-1):
            temp[R-1][i] = temp[R-1][i-1]
        temp[R-1][1] = 0
    else:
        x = s2x+d1x[dir2]
        y = s2y+d1y[dir2]
        while(1):
            nx = x+d1x[dir2]
            ny = y+d1y[dir2]
            if nx==s2x and ny==s2y:
                temp[x][y] = 0
                break
            if s2x<=nx<=R-1 and 0<=ny<C:
                temp[x][y] = temp[nx][ny]
                x = nx
                y = ny
            else:
                dir2 = (dir2+1)%4
    return temp
for i in range(T):
    ground = spread(ground)
    
total = 0
for i in range(R):
    for j in range(C):
        if ground[i][j]!=-1:
            total +=ground[i][j]  
print(total)