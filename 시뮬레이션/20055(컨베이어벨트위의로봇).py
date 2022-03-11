import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
q= deque(map(int,sys.stdin.readline().split()))
robot = deque([0]*N)
count = 0
while(1):
    count+=1
    q.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot)>0:
        for i in range(N-2,-1,-1):
            if robot[i]==1 and robot[i+1]==0 and q[i+1]>0:
                robot[i] = 0
                robot[i+1]=1
                q[i+1]-=1
            robot[-1]=0
    if q[0] >0:
        robot[0]=1
        q[0]-=1
    cnt = q.count(0)
    if cnt>=K:
        print(count)
        break