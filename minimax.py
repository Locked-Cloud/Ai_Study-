tree = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G']
}

scores = {
    'D' : 3,
    'E' : 5,
    'F' : 2,
    'G' : 9
}

def is_terminal(node):
    return node not in tree

def get_children(node):
    return tree.get(node, [])

def minimax(node, depth, is_max, scores, is_terminal):
    if is_terminal(node):
        return scores[node]
    
    if is_max:
        best_score = float('-inf')
        for child in get_children(node):
            score = minimax(child, depth + 1, False, scores, is_terminal)
            best_score = max(best_score, score)
        return best_score
        
    else:
        best_score = float('inf')
        for child in get_children(node):
            score = minimax(child, depth + 1, True, scores, is_terminal)
            best_score = min(best_score, score)
        return best_score
