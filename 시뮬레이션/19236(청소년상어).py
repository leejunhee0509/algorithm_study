import sys
import copy
fish = [-1]*(17)
dx = [-1,-1,0,1,1,1,0,-1] #위 왼 아 오
dy = [0,-1,-1,-1,0,1,1,1]
ground = [[-1]*4 for _ in range(4)]
for i in range(4):
    inf = list(map(int,sys.stdin.readline().split()))
    for j in range(0,len(inf)-1,2):
        num = inf[j]
        dir = inf[j+1]
        ground[i][j//2] = num
        fish[num] = dir-1

start_fish = ground[0][0]
start_dir = fish[start_fish]
fish[start_fish] = -1
ground[0][0] = 0
answer = 0
def find(ground,num):
    for i in range(4):
        for j in range(4):
            if ground[i][j] == num:
                return (i,j)
    return -1

def move(ground, fish, sx,sy,sdir, total):
    global answer
    ground = copy.deepcopy(ground)
    fish = copy.deepcopy(fish)
    for num in range(1,17):
        if find(ground,num)==-1:
            continue
        else:
            x,y = find(ground,num)
            dir = fish[num]
            while(1):
                nx = x+dx[dir]
                ny = y+dy[dir]
                if 0<=nx<4 and 0<=ny<4:
                    if sx==nx and sy==ny:
                        dir = (dir+1)%8
                    else:
                        tmp = ground[nx][ny]
                        ground[nx][ny] = ground[x][y]
                        ground[x][y] = tmp 
                        fish[num] = dir
                        break
                else:
                    dir = (dir+1)%8
    check = False
    while(1):
        sx = sx+dx[sdir]
        sy = sy+dy[sdir]
        if 0<=sx<4 and 0<=sy<4:
            if ground[sx][sy]!=0:
                check = True
                fish_num = ground[sx][sy]
                t = ground[sx][sy]
                ground[sx][sy]= 0
                ndir = fish[fish_num]
                fish[fish_num] = -1
                move(ground,fish,sx,sy,ndir,total+t)
                ground[sx][sy] = t
                fish[fish_num] = ndir
        else:
            break
    if check == False:
        answer = max(answer ,total)
move(ground,fish,0,0,start_dir,start_fish)
print(answer)