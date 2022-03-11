import sys
from math import inf
import math
from collections import deque
N = int(input())
def check(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True   

def bfs(start,target):
    q = deque()
    q.append((start,0))
    visit = [-1]*10000
    visit[start] = 0
    op = [1000,-1000,100,-100,10,-10,1,-1]
    while q:
        num,cnt= q.popleft()
        if num==target:
            return cnt
        num= str(num)

        for i in range(4):
            for j in range(10):
                temp = int(num[:i] + str(j) + num[i+1:])
        # for i in range(8):
        #     temp = num
        #     for j in range(10):
        #         next = temp+op[i]
        #         temp = next
                if 1000<temp<9999 and check(temp):
                    if visit[temp] == -1:
                        visit[temp] = 0
                        q.append((temp,cnt+1))
    return -1

for _ in range(N):
    S,E = map(int,sys.stdin.readline().split())
    flag= bfs(S,E)
    if flag== -1:
        print("Impossible")
    else:
        print(flag)