
def dfs(graph, start):
    if start not in visited:
        visited.add(start)
        path.append(start)
        for node in graph[start]:
            dfs(graph, node)
    return path



graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()
path = []
print(dfs(graph, 'A'))