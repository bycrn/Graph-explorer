from collections import defaultdict, deque
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

# Create a graph instance

# struct of graph edges :{0: [238, 159], 238: [0, 322, 239], .....}
# struct of graph weight = {(s1, S2) : w1, ... , (sk, sn) : wp }

    
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
                

# Algo de prim : arbre couvrant de poid minimal
    # On a un graphe connexe pondéré
    # Input : G(V, E)
    # Output : arbre contenant tous les sommets de poids minimun
    
    # Algorithme :
    #     entrée : graphe, start_node
    #     sortie : arbre couvrant 
        
    # We take any vertx of the graph.
    # At each we will grow this tree.
    #     step 1 : add the edge of minimum weight linked to you vertex.
    #         The chosen edges will be the edges of minimum weights 
    #     step 2 : Check every edge linked to your verteces in you tree 
    #     and verify that the two verteces of this edge are not on the tree already 
    #     add the edge if it's the edge of minimum weight
    #     if there is multiple minimum edge with the same weight, take a random one
        
    #     add weight in the total_weight 
        
    #     if there is no vertices left => End
        
    # Return tree
        
    # ajoute une condition de ne pas mettre une arrete si les deux sommets sont deja dans ma liste
    # ajoute les sommets dans ma liste à la fin 
    # reccurrence

    def prim(self, start_node, list_verteces=None, tree=None):
        if list_verteces is None:
            list_verteces = []
        if tree is None:
            tree = []
        weightsList = []
        edgesList = []

        if self.is_connected():
            if start_node not in list_verteces:
                list_verteces.append(start_node)
            for vertex in list_verteces:
                for edge in self.weights:
                    if edge[0] == vertex:
                        if edge[0] not in list_verteces or edge[1] not in list_verteces:
                            weightsList.append(self.weights[edge])
                            edgesList.append(edge)
            min_weight = weightsList[0]
            index = 0
            for i in range(len(weightsList)):
                if min_weight > weightsList[i]:
                    min_weight = weightsList[i]
                    index = i

            tree.append(edgesList[index])

            for summit in edgesList[index]:
                if summit not in list_verteces:
                    list_verteces.append(summit)

        if len(list_verteces) != self.calculateNbrVertex():
            self.prim(start_node, list_verteces, tree)
            
        return tree

                    
                    
                    
            
            



if __name__ == "__main__":
    # Create a graph instance
    graph = Graph()
    # print(graph.edges,'\n', graph.weights)
    
    start_node = 48

    graph.prim(start_node)
    
    

    # Print the calculated distances

