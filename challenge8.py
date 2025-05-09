class node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def add_node(self, value):
        if value < self.value:
            if not self.left:
                self.set_left(node(value))
            else:
                self.left.add_node(value)
        if value > self.value:
            if not self.right:
                self.set_right(node(value))
            else:
                self.right.add_node(value)
    
    def print_nodes(self):
        if(self.left):
            self.left.print_nodes()
        
        print(self.value)
        
        if(self.right):
            self.right.print_nodes()

    def node_search(self, value, debug = False):
        if debug:
            print(f"Node Search! {self.value}")
        if self.value == value:
            if debug:
                print("Node found!")
            return True
        if self.left and self.value > value:
            if debug:
                print(f"Searching left node to ({self.value})")
            if self.left.node_search(value):
                return True
        if self.right and self.value < value:
            if debug:
                print(f"Searching right node to ({self.value})")
            if self.right.node_search(value):
                return True
        return False
    
    def print_node_structured(self):
        if self.left and self.right:
            print(f"NODE - value: {self.value}, left: {self.left.value}, right: {self.right.value}")
            self.left.print_node_structured()
            self.right.print_node_structured()
        elif self.left:
            
            print(f"LEFT NODE - value: {self.value}, left: {self.left.value}")
            self.left.print_node_structured()
        elif self.right:
            
            print(f"RIGHT NODE - value: {self.value}, right: {self.right.value}")
            self.right.print_node_structured()
        else:
            
            print(f"LEAF NODE - value: {self.value}")

    def node_depth(self):

        left_depth = 0
        right_depth = 0

        if not self.left and not self.right:
            return 0
        if self.left:
            left_depth = 1 + self.left.node_depth()
        if self.right:
            right_depth = 1 + self.right.node_depth()

        return right_depth if right_depth > left_depth else left_depth

    def node_balanced(self):
        left_depth = 0
        right_depth = 0

        if not self.left and not self.right:
            return True
        
        if self.left:
            if not self.left.node_balanced():
                return False
            left_depth = self.left.node_depth()

        if self.right:
            if not self.right.node_balanced():
                return False
            right_depth = self.right.node_depth()

        if abs(left_depth - right_depth) > 1:
            return False
        
        return True
        

class tree:
    def __init__(self, start_node = None):
        self.start_node = start_node

    def add_node(self, value):
        if not self.start_node:
            self.start_node = node(value)
        else:
            self.start_node.add_node(value)

    def print_tree(self):
        if not self.start_node:
            print("Empty")
        else:
            self.start_node.print_nodes()

    def search_tree(self, value):
        if not self.start_node:
            print("Tree is empty")
            return
        
        if self.start_node.node_search(value):
            print(f"The value {value} was found!")
        else:
            print(f"The value {value} was not found!")
        
    def print_tree_structured(self):
        if not self.start_node:
            print("Tree is empty")
            return
        self.start_node.print_node_structured()

    def tree_depth(self):
        if not self.start_node:
            print("Tree is empty")
        else:
            print(f"Tree depth is ({self.start_node.node_depth()})")

    def tree_balanced(self):
        if not self.start_node:
            print("Tree is empty")
            return True
        else:
            return self.start_node.node_balanced()

if __name__ == "__main__":
    mytree = tree()

    """
    mytree.add_node(5)
    mytree.add_node(4)
    mytree.add_node(8)
    mytree.add_node(0)
    mytree.add_node(-1)
    mytree.add_node(2)
    mytree.add_node(-5)
    mytree.add_node(-8)"""
    
    mytree.add_node(5)
    mytree.add_node(4)
    mytree.add_node(7)
    mytree.add_node(8)
    mytree.add_node(9)

    mytree.print_tree()
    mytree.search_tree(2)

    mytree.tree_depth()

    print(f"Balanced Tree: {mytree.tree_balanced()}")
