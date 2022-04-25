from collections import defaultdict


def solution(prd_rels):
    graph = defaultdict(set)
    for prd_list in prd_rels:
        for i in range(len(prd_list)-1):
            for j in range(i+1, len(prd_list)):
                item_a, item_b = prd_list[i], prd_list[j]
                graph[item_a].add(item_b)
                graph[item_b].add(item_a)

    visited = set()
    ans = []

    def dfs(item):
        ret = []
        visited.add(item)
        ret.append(item)

        for i in graph[item]:
            if i not in visited:
                ret += dfs(i)
        return ret

    for rel in prd_rels:
        ret = dfs(rel[0])
        if len(ret) > len(ans):
            ans = ret

    return ans

print(solution([['p1','p2','p3'],['p5','p2'],['p6','p7'],['p8','p7']]))