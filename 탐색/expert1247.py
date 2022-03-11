import sys
from math import inf
T = int(input())
def calc():
    dist = 0
    global answer
    for i in range(N-1):
        idx1 = numbers[i]
        idx2 = numbers[i+1]
        dist += (abs(point[idx2][0] - point[idx1][0])+abs(point[idx2][1]-point[idx1][1]))
    dist += abs(point[numbers[0]][0]-cx) + abs(point[numbers[0]][1]-cy)
    dist += abs(point[numbers[-1]][0] - hx) + abs(point[numbers[-1]][1]-hy)
    answer = min(dist,answer)
    return

def perm(cnt, flag):
    if cnt == N:
        calc()
        return
    for i in range(N):
        if (flag & 1<<i)!=0: 
            continue
        numbers[cnt] = i
        perm(cnt+1, flag | 1<<i)
    


for i in range(T):
    N = int(input())
    answer = inf
    temp = list(map(int,input().split()))
    cx = temp[0]
    cy = temp[1]
    hx = temp[2]
    hy = temp[3]
    point = []
    numbers = [-1]*N
    for j in range(4,len(temp),2):
        point.append((temp[j],temp[j+1]))
    perm(0,0)
    print("#",end="")
    print((i+1),end=" ")
    print(answer)
    
