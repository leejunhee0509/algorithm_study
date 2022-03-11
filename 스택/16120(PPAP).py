import sys

S = input()
if(len(S)==1 and S=='P'):
    print("PPAP")
    exit()
elif(len(S)==1 and S!='P'):
    print("NP")
    exit()
    
stack = []
l = len(S)
for i in range(l):
    if S[i] == 'P':
        stack.append('P')
    else:
        if len(stack)>=2 and i<l-1 and S[i+1]=='P':
            stack.pop()
            stack.pop()
        else:
            print("NP")
            exit()
result = ''.join(stack)
if result=="P" or result=="PPAP":
    print("PPAP")
else:
    print("NP")