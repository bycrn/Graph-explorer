from collections import defaultdict
from data import subway_data

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
        self.add_edge(subway_data)
        self.d = {}
    

    def add_edge(self, subway_data):
        for i in range(len(subway_data['join']['summit1'])):
            from_node = subway_data['join']['summit1'][i]
            to_node = subway_data['join']['summit2'][i]
            weight = subway_data['join']['lon'][i]
        
            self.edges[from_node].append(to_node)
            self.weights[(from_node, to_node)] = weight
            self.edges[to_node].append(from_node)
            self.weights[(to_node, from_node)] = weight
    
    def calculateNbrVertex(self):
        max_vertex = max(self.edges.keys())
        return max_vertex
        

# Bellman-Ford 

# En entrée :  G=(V,E) graphe orienté pondéré et r un sommet de G
# En sortie : Pour chaque sommet u de G un chemin de poids minimal de r vers u

# Initialisations
# Pour i:= 1 à n-1 /* n = nbre de sommets */
#   Relacher tous les arcs de G
# Vérifier qu'il n'y a pas de circuit négatif

#Initialisation 
    # Mettre une etiquette inf sur tous les sommets et une etiquette 0 sur r 

# Relâchement(u,v)
# Si d[v] > d[u] + w(u,v) alors
    # d[v] := d[u] + w(u,v)
    # Parent[v] := u


    def bellman_ford(self, start_node):
        #Initialisation
        self.d = {node: float('inf') for node in self.edges}
        self.d[start_node] = 0
        #Nombre de sommets
        nbrVertex = self.calculateNbrVertex()
        for i in range(1, nbrVertex - 1):
            for from_node, to_nodes in self.edges.items():
                for to_node in to_nodes:
                    if self.d[to_node] > self.d[from_node] + self.weights[(from_node, to_node)]:
                        self.d[to_node] = self.d[from_node] + self.weights[(from_node, to_node)]
                

# Create a graph instance

# struct of graph edges :{0: [238, 159], 238: [0, 322, 239], .....}
# struct of graph weight = {(s1, S2) : w1, ... , (sk, sn) : wp }




if __name__ == "__main__":
    # Create a graph instance
    graph = Graph()
    # print(graph.edges,'\n', graph.weights)
    
    start_node = 48

    graph.bellman_ford(start_node)

    # Print the calculated distances
    print(graph.d)

