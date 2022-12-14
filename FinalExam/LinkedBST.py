from AbstractCollection import AbstractCollection
from BinaryNode import BinaryNode
from LinkedQueue import LinkedQueue


class LinkedBST(AbstractCollection):
	""" A linked binary search tree implementation which uses Nodes """

	def __init__(self):
		self._root = None
		AbstractCollection.__init__(self)

	def find(self, item):
		""" Return data if the item is found or 'None' otherwise """

		def recurse(node):
			if node is None:
				# First Base Case: Item was not found
				return None
			elif item == node.data:
				# Second Base Case: node contains the item!
				return node.data
			elif item < node.data:
				# Recursive Step 1: Move left
				return recurse(node.left)
			else:
				# Recursive Step 2: Move right
				return recurse(node.right)

		return recurse(self._root)

	def add(self, item):
		def recurse(node):
			""" Recursive inner function to find 'item's correct location
			'node' is the root of the tree or subtree being added to """
			if item < node.data:
				# New item being added is less. Go left once if needed
				if node.left is None:
					node.left = BinaryNode(item)
				else:
					recurse(node.left)

			# new item is greater or equal to root, go right if needed
			elif node.right is None:
				node.right = BinaryNode(item)
			else:
				recurse(node.right)

		if self.is_empty():
			# Tree is empty, 'item' becomes the new root
			self._root = BinaryNode(item)
		else:
			# Tree is not empty. Find item's location
			recurse(self._root)

		self._size += 1

	def inorder(self):
		""" Prints the tree with an inorder traversal """
		def recurse(node):
			if node is not None:
				recurse(node.left)
				print(node.data, end=" ")
				recurse(node.right)

		recurse(self._root)

	def postorder(self):
		""" Prints the tree with a postorder traversal """
		def recurse(node):
			if node is not None:
				recurse(node.left)
				recurse(node.right)
				print(node.data, end=" ")

		recurse(self._root)

	def preorder(self):
		""" Prints the tree with a preorder traversal """
		def recurse(node):
			if node is not None:
				print(node.data, end=" ")
				recurse(node.left)
				recurse(node.right)

		recurse(self._root)

	def getSmallest(self):
		""" Returns the smallest element in the tree """
		def recurse(node):
			if node.left is None:
				return node.data
			else:
				return recurse(node.left)

		return recurse(self._root)

	def getLargest(self):
		""" Returns the largest element in the tree """
		def recurse(node):
			if node.right is None:
				return node.data
			else:
				return recurse(node.right)

		return recurse(self._root)

	def height(self):
		return self._root.height()

	def breadth(self):
		""" Prints the tree with a breadth-first traversal """
		queue = LinkedQueue()
		queue.add(self._root)
		while not queue.is_empty():
			node = queue.pop()
			print(node.data, end=" ")
			if node.left is not None:
				queue.add(node.left)
			if node.right is not None:
				queue.add(node.right)


	def is_balanced(self):
		""" Returns True if the tree is balanced """
		def recurse(node):
			if node is None:
				return 0
			else:
				left = recurse(node.left)
				right = recurse(node.right)
				if left == -1 or right == -1 or abs(left - right) > 1:
					return -1
				else:
					return max(left, right) + 1

		return recurse(self._root) != -1

	def balance(self):
		""" Balances the tree """
		if not self.is_balanced():
			# Create a list of the tree's elements
			elements = []
			def recurse(node):
				if node is not None:
					recurse(node.left)
					elements.append(node.data)
					recurse(node.right)
			recurse(self._root)

			# Create a new tree with the elements
			self._root = None
			self._size = 0
			for element in elements:
				self.add(element)