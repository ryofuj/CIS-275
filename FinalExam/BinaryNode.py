class BinaryNode:
	""" Represents a Node in a binary tree """

	def __init__(self, data, left=None, right=None):
		""" By default, this Node will not have any children """

		self.data = data
		self.left = left
		self.right = right

	def height(self):
		""" Returns the height of this Node in the tree """
		if self.left is None and self.right is None:
			return 1
		elif self.left is None:
			return 1 + self.right.height()
		elif self.right is None:
			return 1 + self.left.height()
		else:
			return 1 + max(self.left.height(), self.right.height())

