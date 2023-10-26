from graph import Graph
from data import terminus, subway_data

lines = []


# Function to find directions for each line in the route
def find_directions(transfert, shortest_path):
    direction = []
    for key in transfert :
        print(transfert[key][-2],transfert[key][-1])
        




def print_path(transfer,final_path,time_sp, directions):
    
    text = [f"Vous êtes à {subway_data['stations'][transfer[0][0]][0].upper()}", 
            f"Prenez la ligne {transfer[0][2]} en direction de {subway_data['stations'][directions[0]][0].upper()}"]
    for i in range(len(transfer) - 1):
        for j in range(len(directions)-1):
            if len(transfer) >= 2:
                text.append(f"A {subway_data['stations'][transfer[i][1]][0].upper()}, changez et prenez la ligne {transfer[i+1][2]} en direction de {subway_data['stations'][directions[j+1]][0].upper()}")

    text.append(f"Vous devriez arriver a {subway_data['stations'][final_path[-1]][0].upper()} dans {round((time_sp/60),2)} mn")
    text.append('\n')

    return text


if __name__ == "__main__":
    # Create a graph instance
    graph = Graph()
    
    # Reconstitution des lignes de métro
    
    for line in terminus:
        temp_lines = [line]
        for branch in terminus[line]:
            temp = graph.bellman_ford(branch[0], branch[1])
            temp_lines.append(temp[1])
        lines.append(temp_lines)
            
    print(lines)
    
    # # Check connectivity
    # is_connected = graph.is_connected()
    
    # if is_connected:
    #     print("Le graphe est connecté.")
    # else:
    #     print("Le graphe n'est pas connecté.")
    
    start_node = 48
    destination = 365

    # graph.get_transfert(start_node, destination)
    
    shortest_path = graph.bellman_ford(start_node, destination)[1]
    
    transfert = graph.get_transfert(start_node, destination)

    # Call the function to get directions for each line in your route
    route_directions = find_directions(transfert, shortest_path)

    print(route_directions)

    