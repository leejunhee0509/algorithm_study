import sys
N = int(input())
num = list(map(int,sys.stdin.readline().split()))
answer = [-1]*N
stack = []
for i in range(N-1,-1,-1):
    while len(stack)>0:
        check = stack.pop()
        if num[i]<check:
            answer[i] = check
            stack.append(check)
            break        
    stack.append(num[i])

for x in answer:
    print(x,end = " ")
