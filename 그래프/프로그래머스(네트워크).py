from collections import deque
import heapq
from math import inf
def solution(n, computers):
    dist = [inf]*(n)
    def dijkstra(node):
        dist[node] =0
        q= []
        heapq.heappush(q,(node,0))
        while q:
            cnode, cdist = heapq.heappop(q)
            for i in range(len(computers[cnode])):
                if cnode != i and computers[cnode][i] == 1:
                    distance = cdist+1
                    if dist[i] > distance:
                        dist[i] = distance
                        heapq.heappush(q,(i,distance))
    cnt = 0
    for i in range(len(dist)):
        if dist[i] == inf:
            dijkstra(i)
            cnt+=1
    return cnt
n =3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n,computers)