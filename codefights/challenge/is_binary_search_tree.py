#
# Definition for binary tree:


class Node(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def isBinarySearchTree(tree):
    # build tree from JSON
    # test tree

    def isBST(node):
        return isBSTUtil(node, INT_MIN, INT_MAX)

        # Return true if the given tree is a BST and its values

    # >= min and <= max
    def isBSTUtil(node, mini, maxi):

        # An empty tree is BST
        if node is None:
            return True

        # False if this node violates min/max constraint
        if node.data < mini or node.data > maxi:
            return False

        # Otherwise check the subtrees recursively
        # tightening the min or max constraint
        return (isBSTUtil(node.left, mini, node.data - 1) and
                isBSTUtil(node.right, node.data + 1, maxi))


null = None

tree = {
    "value": 5,
    "left": {"value": 3, "left": {"value": 2, "left": null, "right": null},
             "right": null},
    "right": {
        "value": 8,
        "left": {
            "value": 6,
            "left": null,
            "right": null
        },
        "right": {
            "value": 9,
            "left": null,
            "right": null
        }
    }
}

print(isBinarySearchTree(tree))

# Driver program to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST(root)):
    print("Is BST")
else:
    print("Not a BST")
