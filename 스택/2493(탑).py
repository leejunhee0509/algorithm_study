import sys

N = int(input())
building = list(map(int,sys.stdin.readline().split()))
stack = []

for i in range(N):
    while stack:
        height = stack[-1][1]
        index = stack[-1][0]
        if height<=building[i]:
            stack.pop()
        else:
            stack.append((i+1,building[i]))
            print(index,end = " ")
            break    
    if len(stack)==0:
        print("0",end = " ")
        stack.append((i+1,building[i]))
