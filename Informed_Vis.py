import matplotlib.pyplot as plt
import networkx as nx

# Visualize the uninformed
def visualize_graph(graph, path=None):
    """This is exactly same function as Uninformed_Vis
        But it collects more info including h value 
        in addition to g cost and node childerens.
        Hence it is better for informed search visualizations
    """
    # Create a graph object
    G = nx.DiGraph()
    # iterate over nodes presented in the graph
    for node, childs in graph.items():
        # add each node to the graph with their correspounding costs to each neighbouring nodes
        for info in childs:
            # print(info)
            # print("="*50)
            # 1st modification -----------------------
            child, g, h = info 
            G.add_edge(node, child, weight=g)
            # 2nd modification -----------------------
            G.nodes[node]['h'] = h

    # Use spring_layout to set a random yet consistent position for nodes and their edges 
    position = nx.spring_layout(G, seed=0) # seed stands for random seed
    edge_labels = nx.get_edge_attributes(G, "weight")

    # Create a figure and draw the nodes and their edges
    plt.figure(figsize=(8, 4))
    nx.draw(G, position, with_labels=False, node_color="cyan", node_size=2000, font_size=2)
    nx.draw_networkx_edge_labels(G, position, font_color='red', edge_labels=edge_labels, font_size=10)

    # 3rd modification -----------------------
    node_labels = {}  
    # iterate over nodes
    for node in G.nodes:  
        # and get the heuristic value for each node (or 'N/A' if not available)
        h_cost = G.nodes[node].get('h', 'N/A')  
        label = f"{node}\nH: {h_cost}"  
        node_labels[node] = label  
    # draw the h values for each node
    nx.draw_networkx_labels(G, position, labels=node_labels, font_size=10)
    

    # if a path existed (the user input) , then visualize it using different color coding
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, position, edgelist=path_edges, edge_color="green", width=1.5)

    plt.show()


    # Source: https://networkx.org/documentation/stable/tutorial.html