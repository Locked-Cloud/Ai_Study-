tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

scores = {
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 9
}

def is_terminal(node):
    return node not in tree

def get_children(node):
    return tree.get(node, [])

def alpha_beta_pruning(node, depth, is_max, alpha, beta, scores, is_terminal):
    if is_terminal(node):
        return scores[node]

    if is_max:
        best_score = float('-inf')
        for child in get_children(node):
            score = alpha_beta_pruning(child, depth + 1, False, alpha, beta, scores, is_terminal)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            # Prune if beta is less than or equal to alpha
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for child in get_children(node):
            score = alpha_beta_pruning(child, depth + 1, True, alpha, beta, scores, is_terminal)
            best_score = min(best_score, score)
            beta = min(beta, score)
            # Prune if beta is less than or equal to alpha
            if beta <= alpha:
                break
        return best_score

# Test the Alpha-Beta Pruning implementation
root = 'A'
optimal_value = alpha_beta_pruning(root, 0, True, float('-inf'), float('inf'), scores, is_terminal)
print("Optimal value:", optimal_value)
