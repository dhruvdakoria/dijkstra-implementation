# Dijkstra algorithm implementation in Python
 
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
 
    def add_node(self, value):
        self.nodes.add(value)
 
    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)
 
    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance
 
def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}
 
    nodes = set(graph.nodes)
 
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
 
        if min_node is None:
            break
 
        nodes.remove(min_node)
        current_weight = visited[min_node]
 
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
 
    return visited, path
 
def shortest_path(graph, origin, destination):
    visited, paths = dijsktra(graph, origin)
    full_path = [destination]
    while destination != origin:
        destination = paths[destination]
        full_path.append(destination)
    full_path.reverse()
    return full_path
 
if __name__ == "__main__":
    graph = Graph()
 
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")
    graph.add_node("f")
    graph.add_node("g")
 
    graph.add_edge("a", "b", 2)
    graph.add_edge("a", "c", 5)
    graph.add_edge("a", "d", 1)
    graph.add_edge("b", "e", 2)
    graph.add_edge("c", "e", 5)
    graph.add_edge("c", "f", 3)
    graph.add_edge("d", "b", 3)
    graph.add_edge("d", "g", 1)
    graph.add_edge("e", "g", 2)
    graph.add_edge("f", "g", 5)
 
    print(shortest_path(graph, "a", "g"))