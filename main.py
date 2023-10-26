from graph import Graph
from data import terminus

lines = []


if __name__ == "__main__":
    # Create a graph instance
    graph = Graph()
    
    # Check connectivity
    is_connected = graph.is_connected()
    
    if is_connected:
        print("Le graphe est connecté.")
    else:
        print("Le graphe n'est pas connecté.")
    
    start_node = 48
    destination = 365

    get_all = graph.bellman_ford(start_node, destination)
    print(graph.get_transfert(start_node, destination))
   
    for line in terminus:
        temp_lines = [line]
        for branch in terminus[line]:
            temp = graph.bellman_ford(branch[0], branch[1])
            temp_lines.append(temp[1])
        lines.append(temp_lines)
            
    print(lines)