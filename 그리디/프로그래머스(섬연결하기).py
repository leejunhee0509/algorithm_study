#15 15
def solution(n, costs):
    costs.sort(key = lambda x:x[2])
    cost = costs[0][2]
    routes = set([costs[0][0], costs[0][1]])
    while len(routes)!=n:
        for i in range(len(costs)):
            if costs[i][0] in routes and costs[i][1] in routes:
                continue
            elif costs[i][0] in routes or costs[i][1] in routes:
                routes.update([costs[i][0], costs[i][1]])
                print(routes)
                cost+=costs[i][2]
                break
    return cost
  
n =4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))