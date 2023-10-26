from graph import Graph




if __name__ == "__main__":
    # Create a graph instance
    graph = Graph()
    # print(graph.edges,'\n', graph.weights)
    
    # Check connectivity
    # is_connected = graph.is_connected()
    # if is_connected:
    #     print("Le graphe est connecté.")
    # else:
    #     print("Le graphe n'est pas connecté.")
    
    start_node = 48
    destination = 365

    graph.bellman_ford(start_node, destination)
    
    print(graph.calculateTime(start_node, destination))
    # Print the calculated distances