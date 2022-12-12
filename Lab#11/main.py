from LinkedDirectedGraph import LinkedDirectedGraph
from LinkedQueue import LinkedQueue

graph = LinkedDirectedGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
graph.add_vertex("H")
graph.add_vertex("I")


graph.add_edge("A", "B")
graph.add_edge("A", "D")
graph.add_edge("A", "E")
graph.add_edge("B", "E")
graph.add_edge("D", "G")
graph.add_edge("G", "H")
graph.add_edge("E", "H")
graph.add_edge("E", "F")
graph.add_edge("F", "C")
graph.add_edge("C", "B")
graph.add_edge("H", "I")
graph.add_edge("F", "H")
