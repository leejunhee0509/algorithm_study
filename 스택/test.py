import sys

temp = list(map(str,sys.stdin.readline().strip()))
stack = []
for i in range(len(temp)):
    if temp[i]==')':
        l = 0
        while stack:
            num = stack.pop()
            if num=='(':
                break
            l+=num
        stack.append(stack.pop()*l)
    elif temp[i]=='(':
        stack.append('(')
    elif i<len(temp)-1 and temp[i+1]=='(':
        stack.append(int(temp[i]))
    else:
        stack.append(1)
        
print(sum(stack))