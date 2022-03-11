import sys
test_case = int(input())
for a in range(test_case):
    N,limit = map(int,input().split())
    temp = []
    for _ in range(N):
        favor, cal = map(int,input().split())
        temp.append((favor, cal))
    answer = -1
    visit = [-1]*N
    def dfs(idx, sum1, sum2):
        global answer
        if sum2>limit:
            return
        answer = max(answer, sum1)
        for i in range(idx,N):
            if visit[i] == -1:
                visit[i] = 0
                dfs(i+1, sum1+temp[i][0], sum2+temp[i][1])
                visit[i] = -1
    dfs(0,0,0)
    print("#", end="")
    print(a+1,end =" ")
    print(answer)