class LinkedEdge:
	""" A LinkedEdge represents an edge between two vertices in a directed graph """

	def __init__(self, from_vertex, to_vertex, weight):
		""" 'from_vertex' is the origin, 'to_vertex' is the destination
		'weight' is the weight of the Edge, 0 if using an unweighted graph """
		self._from_vertex = from_vertex
		self._to_vertex = to_vertex
		self._weight = weight

	@property
	def from_vertex(self):
		return self._from_vertex

	@property
	def to_vertex(self):
		return self._to_vertex

	@property
	def weight(self):
		return self._weight

	def __eq__(self, other):
		""" Two edges are equal if they connect the same vertices """
		if self is other:
			return True
		if type(self) != type(other):
			return False
		return self._from_vertex == other.from_vertex and self._to_vertex == other.to_vertex
