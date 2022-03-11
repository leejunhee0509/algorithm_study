import sys
from collections import defaultdict

N = int(sys.stdin.readline())
answer = [-1]*N
num = list(map(int,sys.stdin.readline().split()))
d = defaultdict(int)
for x in num:
    d[x]+=1
stack = []
for i in range(N-1,-1,-1):
    while len(stack)>0:
        check = stack.pop()
        if d[check] > d[num[i]]:
            answer[i] = check
            stack.append(check)
            break
    stack.append(num[i])
    
    
for x in answer:
    print(x,end= " ")