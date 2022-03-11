import sys

temp = list(map(str,sys.stdin.readline().strip()))
cnt1 = 0
cnt2 = 0
for i in range(len(temp)):
    if temp[i]=='(':
        cnt1+=1
    else:
        cnt2+=1
answer=0
def check():
    global answer
    stack = []
    for i in range(len(temp)):
        if temp[i] == '(':
            stack.append(1)
        else:
            if len(stack)==0:
                return
            stack.pop()
    if len(stack)==0:
        answer+=1
    return

for i in range(len(temp)):
    if cnt1>cnt2:
        if temp[i] == '(':
            temp[i]=')'
            check()
            temp[i] = '('
    else:
        if temp[i]==')':
            temp[i]='('
            check()
            temp[i]=')'

print(answer)