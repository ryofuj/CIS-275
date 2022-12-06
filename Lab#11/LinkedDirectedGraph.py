from LinkedVertex import LinkedVertex
from AbstractCollection import AbstractCollection


class LinkedDirectedGraph(AbstractCollection):
	""" Represents an entire directed graph"""

	def __init__(self):
		self._edge_count = 0
		self._vertices = {}
		AbstractCollection.__init__(self)

	def add_vertex(self, label):
		""" Add a vertex to the dictionary with 'label' as the key and a LinkedVertex
		object as the value"""
		self._vertices[label] = LinkedVertex(label)
		self._size += 1

	def get_vertex(self, label):
		""" Retrieves the vertex in this graph with the given label """
		if label in self._vertices:
			return self._vertices[label]
		return None

	def add_edge(self, from_label, to_label, weight=0):
		from_vertex = self.get_vertex(from_label)
		to_vertex = self.get_vertex(to_label)
		from_vertex.add_edge(to_vertex, weight)
		self._edge_count += 1

	def __str__(self):
		return_string = ""
		for vertex in self._vertices.values():
			return_string += str(vertex)

		return return_string
