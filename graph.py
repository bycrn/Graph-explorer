from collections import defaultdict, deque
from data import subway_data


# Création du graphe où on ajoute les arrêtes et les poids 
class Graph():
    def __init__(self):
        # Initialisation de la classe Graph avec des dictionnaires pour stocker les arêtes et les poids
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Méthode pour ajouter une arête avec son poids, en supposant que les arêtes sont bidirectionnelles
        # On ajoute l'arête du nœud de départ au nœud d'arrivée et vice-versa
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        
        # On enregistre le poids de l'arête dans le dictionnaire des poids
        self.weights[(str(from_node), str(to_node))] = weight
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
    
    def bellman_ford(self, start, end):
        pass


# Création de l'instance graphe
graph = Graph()

# Création d'une liste d'arêtes et de leurs poids
edges = list((subway_data['join']['summit1'][i],subway_data['join']['summit2'][i],subway_data['join']['lon'][i])
                    for i in range(len(subway_data['join']['summit1'])))

# Ajout des arêtes au graphe
for edge in edges:
    graph.add_edge(*edge)

print(graph.edges ,'\n\n', graph.weights)



# fonction qui trouve l'id d'une station fonction du nom
def find_id(summit):
    sommet = summit.get().lower()
    for  key in subway_data['stations']:
        if subway_data['stations'][key][0] == sommet:
            node_id = key
    return node_id 




