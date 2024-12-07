def greedy_search(graph, costs, start, goal):
    queue = [start]  
    visited = {}  
    while queue:
        current = queue[0] 
        min_cost = costs.get(current, None) 
        for node in queue[1:]: 
            node_cost = costs.get(node, None)  
            if  node_cost < min_cost:
                current = node  
                min_cost = node_cost
        queue.remove(current) 
        if current == goal:  
            path = []
            while current != start:
                path.append(current)
                current = visited[current]
            path.append(start)
            return path[::-1]  
        for neighbor in graph.get(current, {}):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
    return None  
graph = {
    'A': {'B', 'E'},
    'B': {'A', 'C', 'F'},
    'C': {'B', 'G'},
    'E': {'A', 'D', 'F'},
    'F': {'B', 'E', 'G'},
    'G': {'C', 'F', 'H'},
    'H': {'D', 'G'}
}
costs = {
    'A': 1,
    'B': 2,
    'C': 1,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 2,
    'H': 1
}
start = 'A'
goal = 'H'
path = greedy_search(graph, costs, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
