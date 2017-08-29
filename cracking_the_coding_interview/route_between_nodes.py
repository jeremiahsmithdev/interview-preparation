#ccti 4.1

#leverage bfs (or dfs)
def route_between_nodes(a, b):
    queue = [a]
    while len(queue) > 0:
        current_node = queue.pop(0)
        for adj_node in get_adj_nodes(current_node):
            if not adj_node.visited:
                queue.append(adj_node)
        if adj_node.key == b.key:
            return True
        current_node.visited = True
    return False
