import sys

N,K = map(int,sys.stdin.readline().split())
answer = 0
word = [set(sys.stdin.readline().rstrip()) for _ in range(N)]
if K<5:
    print(0)
    exit()
elif K==26:
    print(N)
    exit()
    
pick = [0]*26
for c in ('a','c','i','n','t'):
    pick[ord(c)-ord('a')] =1

def dfs(idx, cnt):
    global answer
    if cnt == K-5:
        count = 0
        for temp in word:
            check = True
            for alpha in temp:
                if not pick[ord(alpha)-ord('a')]:
                    check = False
                    break
            if check:
                count+=1
        answer = max(answer, count)           
        return
    for i in range(idx,26):
        if not pick[i]:
            pick[i]=1
            dfs(i+1,cnt+1)
            pick[i]=0
dfs(0,0)
print(answer)
