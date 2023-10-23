from collections import defaultdict, deque
from data import subway_data


# Création du graphe où on ajoute les arrêtes et les poids 
class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
        self.add_edge(subway_data)

    def add_edge(self, subway_data):
        for i in range(len(subway_data['join']['summit1'])):
            from_node = subway_data['join']['summit1'][i]
            to_node = subway_data['join']['summit2'][i]
            weight = subway_data['join']['lon'][i]
        
            self.edges[from_node].append(to_node)
            self.weights[(from_node, to_node)] = weight
            self.edges[to_node].append(from_node)
            self.weights[(to_node, from_node)] = weight

    
    def is_connected(self):
        if not self.edges:
            return False

        starter = list(self.edges.keys())[0]
        visited = set()
        queue = deque([starter])

        while queue:
            sommet = queue.popleft()
            visited.add(sommet)
            for neighbor in self.edges[sommet]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
        return len(visited) == len(self.edges) 
    
    def bellman_ford(self, start_node):
        pass


# Création de l'instance graphe
graph = Graph()

# Check connectivity
is_connected = graph.is_connected()
if is_connected:
    print("Le graphe est connecté.")
else:
    print("Le graphe n'est pas connecté.")




# # print(graph.edges ,'\n\n', graph.weights)

# start_node = 0  # Replace with the desired starting node
# shortest_paths = graph.bellman_ford(start_node)

# # print(shortest_paths)
# # Print the shortest paths
# for node, distance in shortest_paths.items():
#     print(f"Distance from {start_node} to {node}: {distance}")



# # fonction qui trouve l'id d'une station fonction du nom
# def find_id(summit):
#     sommet = summit.get().lower()
#     for  key in subway_data['stations']:
#         if subway_data['stations'][key][0] == sommet:
#             node_id = key
#     return node_id 




