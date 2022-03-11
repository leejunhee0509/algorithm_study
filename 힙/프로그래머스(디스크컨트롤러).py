def solution(jobs):
    jobs.sort(key = lambda x:x[1])
    now = 0
    answer = 0
    l = len(jobs)
    while len(jobs)>0:
        check = False
        for i in range(len(jobs)):
            if jobs[i][0]<=now:
                now += jobs[i][1]
                answer += now - jobs[i][0]
                jobs.pop(i)
                check = True
                break
        if check == False:
            now +=1
    return answer//l

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))