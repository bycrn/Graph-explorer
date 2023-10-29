from graph import Graph
from data import terminus, subway_data, lines






# Function to find directions for each line in the route
def find_directions(transfert, lines):
    direction, directions  = [], []
    for key in transfert :
        for line in lines :
            if key == line[0]:
                for i in range(1,len(line)):
                    if transfert[key][-2][0] in line[i]:
                        index = line[i].index(transfert[key][-2][0])
                        if transfert[key][-1][0] == line[i][index + 1]:
                            direction.append(line[i][-1])
                            break
                        if transfert[key][-1][0] == line[i][index - 1]:
                            direction.append(line[i][0])
                            break
    for ids in direction:
        for key, values in subway_data['stations'].items():
            if ids == key:
                directions.append(values[0])
            
    return direction


def findname(directions):
    convert = []
    for id_station in directions :
        for station_id, info in subway_data['stations'].items():
            if id_station == station_id:
                convert.append(info[0])
    return convert

if __name__ == "__main__":
    # Create a graph instance
    graph = Graph()
    
    # Reconstitution des lignes de métro
    
    

    
    # # Check connectivity
    # is_connected = graph.is_connected()
    
    # if is_connected:
    #     print("Le graphe est connecté.")
    # else:
    #     print("Le graphe n'est pas connecté.")
    
    start_node = 1
    destination = 97

    # graph.get_transfert(start_node, destination)
    
    shortest_path = graph.bellman_ford(start_node, destination)[1]
    
    transfert = graph.get_transfert(start_node, destination)
    
    time_sp = graph.calculateTime(start_node, destination)

    # Call the function to get directions for each line in your route
    route_directions = find_directions(transfert)
    
    
    print(shortest_path,"\n","\n",transfert,"\n","\n",time_sp,"\n","\n",route_directions,"\n",)
    
    print(findname(route_directions))
  

    