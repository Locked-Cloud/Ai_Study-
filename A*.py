graph = {
    'S' : [('A', 1), ('B', 4)],
    'A' : [('B', 2), ('C', 5), ('G', 12)],
    'B' : [('C', 2)],
    'C' : [('G', 3)],
}
H_TABLE = {
    'S' : 7,
    'A' : 6,
    'B' : 4,
    'C' : 2,
    'G' : 0
}

# Function to calculate the f_cost for a given path
def path_f_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_TABLE[last_node]
    f_cost = g_cost + h_cost
    return f_cost

def A_star(graph, start, goal):
    visited = [] 
    queue = [([('S', 0)], 0)]  # Initialize the queue with the start node and its cost
    
    while queue:
        queue.sort(key=lambda x: path_f_cost(x[0]))  # Sort queue by f_cost

        path, g_cost = queue.pop(0)  # Pop the path with the lowest f_cost
        node = path[-1][0]  # Get the last node of the path
        
        if node in visited:
            continue
        
        visited.append(node)
        
        if node == goal:
            return [x[0] for x in path]  # Return the path (only node names)
        
        else:
            adjacent_nodes = graph.get(node, [])
            for next_node, cost in adjacent_nodes:
                new_path = path.copy()
                new_path.append((next_node, cost))
                queue.append((new_path, g_cost + cost))  # Append new path with updated g_cost

# Run the A* search
solution = A_star(graph, 'S', 'G')
print('Path is: ', solution)
