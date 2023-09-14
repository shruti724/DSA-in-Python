def addEdges(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def printGraph(adj):
    for _ in adj:
        print(_)


# no. of vertices
V = 4
# adjacency list using dynamic list in python
adj = [[] for i in range(V)]
addEdges(adj, 1, 3)
addEdges(adj, 2, 1)
addEdges(adj, 0, 3)
printGraph(adj)
