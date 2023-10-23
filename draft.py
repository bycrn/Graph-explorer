from collections import defaultdict
from data import subway_data

class Graph:
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

    def bellman_ford(self, start_node):
        pass

# Create a graph instance
graph = Graph()

    
print(graph.edges, graph.weights)


# print(graph.bellman_ford('276'))
