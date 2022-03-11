# 15 19
def solution(routes):
    routes.sort(key=lambda x:x[0])
    cnt = 1
    p1 = routes[0][0]
    p2 = routes[0][1]
    for info in routes:
        start = info[0]
        end = info[1]
        if start>p1:
            p1 = start
        if end<p2:
            p2 = end
        if start>p2:
            cnt+=1
            p1 = start
            p2 = end
    return cnt
routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)