graph = {
    'S' : ['A','B','C'],
    'A' : ['B','C','G'],
    'C' : ['D'],
    'G' : ['D'],
    'D' : ['G'],
}

def bfs(graph, start, goal):
    visited = [] 
    queue = [[start]]
    
    while queue:
        path = queue.pop(0)  
        print(path)
        node = path[-1]
        
        if node in visited:
            continue
        
        visited.append(node)
        
        if node == goal:
            return path
        
        else:
            adjacent_nodes = graph.get(node, [])
            for node2 in adjacent_nodes:
                new_path = path.copy() 
                new_path.append(node2)
                queue.append(new_path)  

solution = bfs(graph, 'S', 'G')
print('Path is: ', solution)
