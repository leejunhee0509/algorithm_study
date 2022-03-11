import sys

S = input()
target = input()
stack = []
l = len(target)
check = target[-1]

for last in S:
    stack.append(last)
    if last == check and ''.join(stack[-l:]) == target:
        del stack[-l:]
        
answer=  ''.join(stack)
if len(answer)==0:
    print("FRULA")
else:
    print(answer)