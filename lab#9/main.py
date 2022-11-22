from LinkedBST import LinkedBST

def main():
    tree = LinkedBST()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    tree.inorder()
    print()
    tree.preorder()
    print()
    tree.postorder()
    print()
    '''find'''
    print(tree.find(5))
    print(tree.find(3))
    print(tree.find(7))

if __name__ == "__main__":
    main()
