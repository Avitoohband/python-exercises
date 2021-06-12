class AVLNode:

    # this class represent an AVL Node
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value
        self.height = 0  # the height of the node
        self.bf = 0  # the balance factor of the node

    # returns tye left child of the node
    def get_right(self):
        return self.right

    # returns the left child of the node
    def get_left(self):
        return self.left

    # return the value of the node
    def get_value(self):
        return self.value

    # return the height of the node
    def get_height(self,):
        return self.height


class AVLTree:

    # this class represent an AVL tree
    def __init__(self):
        self.root = None  # the root Node of the tree
        self.node_count = 0

    # returns the height of the tree
    def get_height(self):
        if self.root is None:
            return 0
        return self.root.get_height()

    # returns whether or not the tree is empty
    def is_empty(self):
        return self.height == 0

    # checks if a certain value is exist
    # in the tree and returns true\false respectively
    def contains(self, value):
        return self.contains_helper(self.root, value)

    # recursive contain heper metohd
    def contains_helper(self, node, value):
        if node is None:
            return False

        cmp = int(value - node.value)
        if cmp < 0:  # the value is smaller than the node value
            self.contains(node.left, value)
        if cmp > 0:  # the value is bigger than the node value
            self.contains(node.right, value)

        return True


    # Insert a vlaue to the AVL tree
    # Running Time = O(log(n))
    def insert(self, value):
        if value is None:
            return False
        if not self.contains(value):
            self.root = self.inset_helper(self.root, value)
            self.node_count += 1
            return True
        return False # if the value is already is in the AVL tree

    # Insert method helper, add the value to the AVL Tree
    def inset_helper(self, node, value):
        if node is None:
            return AVLNode(None, None, value)

        cmp = int(value - node.value)
        if cmp < 0:  # the value is smaller than the node value
            self.inesrt_helper(node.left, value)
        else:  # the value is bigger than the node value
            self.inesrt_helper(node.right, value)

         # update Balance factor and the Height
        self.update(node)
         # re-balance the tree
        return self.balance(node)

    # updates the Balance factor and the height value of a node
    def update(self, node):
        left_node_height = -1
        right_node_height = -1
        if node.left is not None:
            left_node_height = node.left.height
        if node.right is not None:
            right_node_height = node.right.height

        # update the current node's height
        node.height = 1 + max(left_node_height, right_node_height)

        # update this node's Blanace factor
        node.bf = right_node_height - left_node_height

    # re-balance the node if the balance factor isn't -1 to 1
    def balance(self, node):
        if node.bf == -2:  # left heavy case
            if node.leff.bf <= 0:  # left-left case
                return self.left_left_case(node)
            else:  # left-right case
                return self.left_right_case(node)
        elif node.bf == 2:  # right heavy case
            if node.right.bf >= 0:  # right-right caase
                return self.right_right_case(node)
            else:  # right-left case
                return self.right_left_case(node)
        # if either bf's of the node aren't 2 or -2 then
        # we have a bf of -1 to 1, so its balanced
        return node

    def left_left_case(self, node):
        return self.right_rotation(node)  # rotate the left to the right

    def left_right_case(self, node):
        node.left = self.left_rotation(node.left)  # make the case to be left-left case
        return self.right_rotation(node)

    def right_right_case(self, node):
        return self.left_rotation(node)  # rotate the right to the left

    def right_left_case(self, node):
        node.right = self.right_rotation(node)  # make the case to be right-right case
        return self.left_rotation(node)

    def left_rotation(self, node):
        new_parent = node.right
        node.right = new_parent.left
        new_parent.left = node
        self.update(node)
        self.update(new_parent)
        return new_parent