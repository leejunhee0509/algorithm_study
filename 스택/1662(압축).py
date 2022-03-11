import sys
s = list(map(str,sys.stdin.readline().strip()))
stack = []

for i in range(len(s)):
    if s[i]=="(":
        stack.append("(")
    elif s[i]==")":
        cnt = 0
        while True:
            temp = stack.pop()
            if temp=="(":
                break
            cnt+=temp
        stack.append(int(stack.pop())*cnt)
    elif i<len(s)-1 and s[i+1]=="(":
        stack.append(int(s[i]))
    else:
        stack.append(1)
print(sum(stack))
        
            