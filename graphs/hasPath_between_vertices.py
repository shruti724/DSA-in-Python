def DFSRec(adj, s, visited):
    visited[s] = True
    for u in adj[s]:
        if visited is False:
            DFSRec(adj, u, visited)


def DFS(adj, s):
    visited = [False]*len(adj)
    DFSRec(adj, s, visited)


def hasPath(adj, s):
    lis = []
    # pathExits = False
    lis.append(DFS(adj, s))
    # if u in DFS(adj, s):
    #     return pathExits is True
    # else:
    #     return pathExits
    return lis


adj = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [1, 2, 4], [2, 3]]
print(hasPath(adj, 0))
