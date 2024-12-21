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

/////////////////////////////////////////////

def GreedyBestFirst(graph, start, goal):
    def path_h_cost(path):
        return h_table[path[-1]]

    done = []
    queue = [[start]]
    while queue:
        queue.sort(key=path_h_cost)  
        path = queue.pop(0)  # Select the path with the lowest heuristic
        node = path[-1]  # Get the last node in the current path

        if node in done:
            continue
        done.append(node)

        if node == goal:
            return path  # Goal reached, return the path

        adj_nodes = graph.get(node, [])
        for node2 in adj_nodes:
            if node2 not in done:  # Avoid revisiting nodes
                newpath = path + [node2]
                queue.append(newpath)

    return None  # If no path is found

# Example usage
My_graph = {
    "S": ["A", "B"],
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["G"],
    "D": ["G"],
    "G": []
}

h_table = {
    "S": 7,
    "A": 6,
    "B": 2,
    "C": 1,
    "D": 1,
    "G": 0
}

print("The path by Greedy Best-First Search is:", GreedyBestFirst(My_graph, "S", "G"))



////////////////////////////////////////////////////////

def GreedyBestFirst(graph, start, goal):
    visited = []   # To keep track of visited nodes
    queue = [[start]]  # Paths to explore
    
    while queue:
        # Sort the queue by the heuristic value of the last node in each path
        queue.sort(key=lambda path: h_table[path[-1]])
        path = queue.pop(0)  # Get the path with the smallest heuristic value
        node = path[-1]      # Current node

        if node in visited:  # Skip if already visited
            continue
        visited.append(node)

        if node == goal:     # Return path if goal is reached
            return path

        # Add neighbors to the queue
        adjacent_nodes = graph.get(node, [])
        for node2 in adjacent_nodes:  # Added the missing colon here
            if node2 not in visited:
                queue.append(path + [node2])

    return None  # Return None if no path is found

# Example usage
My_graph = {
    "S": ["A", "B"],
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["G"],
    "D": ["G"],
    "G": []
}

h_table = {
    "S": 7,
    "A": 6,
    "B": 2,
    "C": 1,
    "D": 1,
    "G": 0
}

print("The path by Greedy Best-First Search is:", GreedyBestFirst(My_graph, "S", "G"))
