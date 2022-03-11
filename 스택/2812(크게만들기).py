import sys

N,K = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().strip()))
stack = []
for i in range(N):
    while K>0 and stack:
        if stack[-1]<num[i]:
            stack.pop()
            K-=1
        else:
            break
    if K==0:
        stack+=num[i:]
        break
    stack.append(num[i])
for i in range(len(stack)-K):
    print(stack[i],end="")

