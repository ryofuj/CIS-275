from LinkedEdge import LinkedEdge


class LinkedVertex:
	""" Represents a vertex in a linked, directed graph """

	def __init__(self, label):
		""" edge_list will contain LinkedEdge objects to represent edges originating
		from this Vertex. _visited is 'True' if this vertex has been visited in current traversal """
		self._edge_list = []
		self._label = label
		self._visited = False

	def neighboring_vertices(self):
		""" Returns an iterator over the vertices that 'self' directly connects to """

		# 'vertices' will be a list of every vertex 'self' directly connects to
		vertices = []

		# Iterate over the list of edges, adding each 'to' vertex to the list
		for edge in self._edge_list:
			vertices.append(edge.to_vertex)

		return iter(vertices)

	def add_edge(self, to_vertex, weight):
		""" Adds an edge from this vertex to 'to_vertex' with the given weight """
		new_edge = LinkedEdge(self, to_vertex, weight)
		self._edge_list.append(new_edge)

	def get_edge(self, to_vertex):
		""" Returns the edge that connects 'self' to 'to_vertex', or None if it doesn't exist """
		for edge in self._edge_list:
			if edge.to_vertex == to_vertex:
				return edge

		return None

	def set_visited(self):
		self._visited = True

	def clear_visited(self):
		self._visited = False

	@property
	def label(self):
		return self._label

	@property
	def visited(self):
		return self._visited

	def __str__(self):
		return_string = "Label: " + str(self._label) + "\n"
		for edge in self._edge_list:
			return_string += "\tFrom: " + str(self._label)
			return_string += " To: " + str(edge.to_vertex.label)
			return_string += " Weight: " + str(edge.weight) + "\n"

		return return_string

