# DFS : Depth First Search

def dfs(graph, root, goal):
    open_list = [root] # Same as BFS
    closed_list = [] 

    # While the Frontier is not empty, do:
    while open_list: 
        # LIFO: Remove the Latest input to the Frontier and expand it
        current_node = open_list.pop()
        # Is it the goal?
        if current_node == goal: 
            closed_list.append(current_node)
            break

        # if the expanding node is new (wasnt previously expanded)
        if current_node not in closed_list:
            # then added to the closed list (expand it)
            closed_list.append(current_node)
            # and add its children to the frontier in reverse format (LIFO)
            for child, _ in reversed(graph[current_node]):
                if child not in closed_list and child not in open_list:
                    open_list.append(child)

    return closed_list