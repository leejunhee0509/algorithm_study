import sys
import heapq
from math import inf
N = int(input())

fr = [[] for _ in range(N+1)]
while(1):
    a,b = map(int,sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    else:
        fr[a].append(b)
        fr[b].append(a)
answer= []
def dijkstra(node):
    global answer
    dist = [inf]*(N+1)
    dist[node] = 0
    dist[0] = 0
    q = []
    heapq.heappush(q, [0,node])
    while q:
        cdist, cnode = heapq.heappop(q)
        if dist[cnode] < cdist:
            continue
        for nextnode in fr[cnode]:
            distance = dist[cnode]+1
            if dist[nextnode]>distance:
                dist[nextnode] = distance
                heapq.heappush(q,[distance,nextnode])
    temp = max(dist)
    answer.append((node,temp))
for i in range(1,N+1):
    dijkstra(i)
answer.sort(key = lambda x:(x[1],x[0]))
check = answer[0][1]
cnt = 0
a = []
for node, score in answer:
    if score>check:
        break
    cnt+=1
    a.append(node)
print(check,cnt)
for item in a:
    print(item, end=" ")
