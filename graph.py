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







