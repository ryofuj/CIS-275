"""
Ryo Fujimura
CIS 275C
Final
"""

from LinkedBST import LinkedBST
from BinaryNode import BinaryNode

def main():
	# Create a tree
	tree = LinkedBST()
	tree.add(5)
	tree.add(3)
	tree.add(7)
	tree.add(2)
	tree.add(4)
	tree.add(6)
	tree.add(8)

	# Print the tree
	print("Inorder:", end=" ")
	tree.inorder()
	print()
	print("Preorder:", end=" ")
	tree.preorder()
	print()
	print("Postorder:", end=" ")
	tree.postorder()
	print()

	# Test find
	print("Find 5:", tree.find(5))
	print("Find 3:", tree.find(3))
	print("Find 7:", tree.find(7))
	print("Find 2:", tree.find(2))
	print("Find 4:", tree.find(4))	
	print("Find 6:", tree.find(6))
	print("Find 8:", tree.find(8))
	print("Find 1:", tree.find(1))
	print("Find 9:", tree.find(9))

	# Test getSmallest and getLargest
	print("Smallest:", tree.getSmallest())
	print("Largest:", tree.getLargest())

    # Test height
	print("Highest:", tree.height())

	# Test breadth

	# Test isBalanced
	print("isBalanced:", tree.is_balanced())

	# Test Balance
	tree.balance()
	print("Balance:", tree.balance())



if __name__ == "__main__":
	main()