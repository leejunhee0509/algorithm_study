import sys
import itertools

expression = list(map(str,sys.stdin.readline().strip()))
stack, pos, answer = [],[],set()

for i,value in enumerate(expression):
    if value=='(':
        stack.append(i)
    if value==')':
        pos.append((stack.pop(),i))

for i in range(1,len(pos)+1):
    comb = list(itertools.combinations(pos,i))
    for j in comb:
        temp = list(expression)
        for x,y in j:
            temp[x]=''
            temp[y]=''
        answer.add(''.join(temp))

for x in sorted(list(answer)):
    print(x)
        