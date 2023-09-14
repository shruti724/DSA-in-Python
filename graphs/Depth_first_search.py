def DFSRec(adj, s, visited):
    visited[s] = True
    print(s, end=" ")
    for u in adj[s]:
        if visited[u] is False:
            DFSRec(adj, u, visited)
            visited[u] = True


def DFS(adj, s):
    visited = [False] * len(adj)
    DFSRec(adj, s, visited)


s = 0
adj = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [1, 2, 4], [2, 3]]
DFS(adj, s)
