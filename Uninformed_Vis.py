import matplotlib.pyplot as plt
import networkx as nx

# Visualize the uninformed
def visualize_graph(graph, path=None):
    """This Function takes a graph and also a path as an input and visualizes the path on the aformentioned graph
        ---------------------------------------------
        graph: input graph
        path: path to visualize
    """
    # Create a graph object
    G = nx.DiGraph()
    # iterate over nodes presented in the graph
    for node, childs in graph.items():
        # add each node to the graph with their correspounding costs to each neighbouring nodes
        for child, cost in childs:
            G.add_edge(node, child, weight=cost)

    # Use spring_layout to set a random yet consistent position for nodes and their edges 
    position = nx.spring_layout(G, seed=0) # seed stands for random seed
    edge_labels = nx.get_edge_attributes(G, "weight")

    # Create a figure and draw the nodes and their edges
    plt.figure(figsize=(8, 4))
    nx.draw(G, position, with_labels=True, node_color="cyan", node_size=500, font_size=8)
    nx.draw_networkx_edge_labels(G, position, font_color='red', edge_labels=edge_labels, font_size=10)

    # if a path existed (the user input) , then visualize it using different color coding
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, position, edgelist=path_edges, edge_color="green", width=1.5)

    plt.show()


    # Source: https://networkx.org/documentation/stable/tutorial.html