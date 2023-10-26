from graph import Graph
from data import subway_data




if __name__ == "__main__":
    # Create a graph instance
    graph = Graph()
    # print(graph.edges,'\n', graph.weights)
    
    # Check connectivity
    is_connected = graph.is_connected()
    if is_connected:
        print("Le graphe est connecté.")
    else:
        print("Le graphe n'est pas connecté.")
    
    start_node = 48
    destination = 365

    get_all = graph.bellman_ford(start_node, destination)
    start_node = 7
    print(graph.get_transfert(start_node, destination))
    prime = graph.prim(start_node)
    print(prime)
    
    # Print the calculated distances