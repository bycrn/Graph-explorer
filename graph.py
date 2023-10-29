from collections import defaultdict, deque
from data import subway_data


# Création du graphe où on ajoute les arrêtes et les poids 
class Graph():
    def __init__(self):
        
        # Create a graph instance
            # struct of graph edges :{0: [238, 159], 238: [0, 322, 239], .....}
            # struct of graph weight = {(s1, S2) : w1, ... , (sk, sn) : wp }

        self.edges = defaultdict(list)
        self.weights = {}
        self.add_edge(subway_data)

    def add_edge(self, subway_data):
        for i in range(len(subway_data['join']['summit1'])):
            from_node = subway_data['join']['summit1'][i]
            to_node = subway_data['join']['summit2'][i]
            weight = subway_data['join']['lon'][i]
        
            self.edges[from_node].append(to_node)
            self.edges[to_node].append(from_node)
            self.weights[(from_node, to_node)] = weight
            self.weights[(to_node, from_node)] = weight

    def calculateNbrVertex(self):
        max_vertex = max(self.edges.keys())
        return max_vertex
    
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
    
    # Bellman-Ford 

        # En entrée :   - G=(V,E) graphe orienté pondéré et 
        #               - r un sommet de G
        # En sortie : Pour chaque sommet u de G un chemin de poids minimal de r vers u

        # Step 1 Initialisations
        # step 2 Pour i:= 1 à n-1 /* n = nbre de sommets */
        #            Relacher tous les arcs de G
        # Step 3 Vérifier qu'il n'y a pas de circuit négatif

        #Initialisation (step 1)
            # Mettre une etiquette inf sur tous les sommets et une etiquette 0 sur r 

        # Relâchement(u,v)(step 2)
        # Si d[v] > d[u] + w(u,v) alors
            # d[v] := d[u] + w(u,v)
            # Parent[v] := u
    
    def bellman_ford(self, start_node, destination):
        # Initialize distances and parents
        self.d = {node: float('inf') for node in self.edges}
        self.d[start_node] = 0
        parents = {node: None for node in self.edges}

        #ONE TO ALL
        
        # Number of vertices
        nbrVertex = self.calculateNbrVertex()

        for i in range(1, nbrVertex - 1):
            for from_node, to_nodes in self.edges.items():
                for to_node in to_nodes:
                    if self.d[to_node] > self.d[from_node] + self.weights[(from_node, to_node)]:
                        self.d[to_node] = self.d[from_node] + self.weights[(from_node, to_node)]
                        parents[to_node] = from_node  # Update the parent


        # RETRIEVE PATH ONE TO ONE 
      
        shortest_path = []
        while destination is not None:
            shortest_path.insert(0, destination)
            destination = parents[destination]

        
        return (self.d, shortest_path)
    
    


    def calculateTime(self, start_node, destination):
        temp = self.bellman_ford(start_node, destination)
        for key in temp[0]:
            if destination == key:
                return int(temp[0][key]/60)
            
    # A partir du chemin récupéré, je reconstitue les transferts avec les lignes
    
    def get_transfert(self, start_node, destination):
        temp = self.bellman_ford(start_node, destination)
        transfert = {}
        for ID in temp[1]:
            for stationID, statinfo in subway_data['stations'].items() :
                if stationID == ID :
                    if statinfo[1] in transfert:
                        transfert[statinfo[1]].append((ID, statinfo[0]))
                    else : transfert[statinfo[1]] = [(ID, statinfo[0])] 
        
        return transfert

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
            
        #     if there is no vertices left 
        #           => End
        #           Return tree
        #     else recurrence
            
       

    def prim(self, start_node, list_vertices=[], tree=[]):
        if not self.is_connected():
            return tree

        weightsList = []
        edgesList = []

        if start_node not in list_vertices:
            list_vertices.append(start_node)

        for vertex in list_vertices:
            for edge in self.weights:
                if edge[0] == vertex and edge[1] not in list_vertices:
                    weightsList.append(self.weights[edge])
                    edgesList.append(edge)

        if not weightsList:  # If weightsList is empty, return the current tree
            return tree

        min_weight = weightsList[0]
        index = 0
        for i in range(len(weightsList)):
            if min_weight > weightsList[i]:
                min_weight = weightsList[i]
                index = i

        tree.append(edgesList[index])

        for summit in edgesList[index]:
            if summit not in list_vertices:
                list_vertices.append(summit)

        if len(list_vertices) <= self.calculateNbrVertex():
            self.prim(start_node, list_vertices, tree)

        return tree

