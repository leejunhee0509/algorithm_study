import sys
from collections import deque
V= int(input())
tree = [[] for _ in range(V+1)]
for i in range(V):
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(temp)-2,2):
        tree[i+1].append((temp[j],temp[j+1]))

def bfs(n):
    answer = [0,0]
    visit = [-1]*(V+1)
    visit[n] = 0
    q = deque()
    q.append(n)
    while q:
        node = q.popleft()
        for next_node, next_dist in tree[node]:
            if visit[next_node] == -1:
                q.append(next_node)
                visit[next_node] = visit[node]+next_dist
                if answer[1]<visit[next_node]:
                    answer[1] = visit[next_node]
                    answer[0] = next_node
    return answer
node, dis = bfs(2)
node, dis = bfs(node)
print(dis)

    