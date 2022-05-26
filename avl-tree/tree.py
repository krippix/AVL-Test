class Tree():

    def __init__(self, value=None):
        '''Creates new tree root'''
        
        self.value = value
        self.left = None
        self.right = None
        self.balance = 0
        
        # This variable cannot be trusted and is relative!
        self.depth = 0
    

    def insert(self, value):
        '''Insert value into current tree'''

        # if list was provided, just iterate over it multiple times
        if isinstance(value, list):
            for no in value:
                self.insert(no)
            return
        
        if self.value is None:
            self.value = value
        
        if value == self.value:
            print("Value already in searchtree")

        Tree.__rec_insert(self, value)

    
    def __rec_insert(tree, value):
        
        # left
        if value < tree.value:
            if tree.left is None:
                tree.left = Tree(value)
                return
            tree.left.insert(value)
            
        # right
        if value > tree.value:
            if tree.right is None:
                tree.right = Tree(value)
                return
            tree.right.insert(value)

        # while going back up, check if each node is balanced
        Tree.calc_balance(tree)
    


    
    def search(self, value) -> bool:
        '''Check if item is in tree'''

        if value == self.value:
            return True

        # left
        if value < self.value:
            if self.left is None:
                return False
            return self.left.search(value)

        # right
        if value > self.value:
            if self.right is None:
                return False
            return self.right.search(value)

    
    def __search_parent(tree, child):
        '''Searches for parent node of provided value. Make sure result is not in the root of the tree you provide.'''

        # left
        if child.value < tree.value:
            if tree.left.value == child.value:
                return tree
            next_tree = tree.left
        
        # right
        if child.value > tree.value:
            if tree.right.value == child.value:
                return tree
            next_tree = tree.right

        return Tree.__search_parent(next_tree, child)


    def delete(self, value) -> bool:
        
        if self.value == value:
            # this should only happen if this is the root of the tree
            print("Deleting root node")
            result = self.__delete_root()
            return

        result = Tree.__delete_node(self, value)
        
        if not result:
            print("Node not found, nothing deleted.")
        return result
     

    def __delete_node(tree, value):
        '''Deletion of any node that is not the root node'''
        
        if value < tree.value:
            next_node = tree.left
        else:
            next_node = tree.right

        if next_node is None:
            return False

        if next_node == value:
            tree.right = Tree.find_successor_parent(next_node)
            return True
        
        return Tree.__delete_node(next_node, value)
        

    def __delete_root(self):
        if self.right is None and self.left is None:
            print("This is the only node available.")
            self.value == None
            return True
            
        # right is None
        if self.right is None:
            self.value = self.left.value
            self.right = self.left.right
            self.left = self.left.left
            return True
        
        # left is None
        if self.left is None:
            self.value = self.right.value
            self.left = self.right.left
            self.right = self.right.right
            return True

        # right.left None
        if self.right.left is None:
            self.value = self.right.value
            self.right = self.right.right
            return True

        # if none of the trivial cases worked
        successor = Tree.find_successor(self)
        parent = Tree.__search_parent(self, successor)

        # successor should always be left of parent.
        parent.left = successor.right
        self.value = successor.value
        

    def find_successor(tree):
        '''Returns successor for given tree's root. Entrypoint.'''

        if tree.right.left is None:
            return tree.right
        
        return Tree.__rec_find_successor(tree.right.left)


    def __rec_find_successor(tree):
        '''Returns successor for given tree's root. Dont call this.'''

        if tree.left is None:
            return tree
        
        return Tree.__rec_find_successor(tree.left)
        

    def calc_depth(self):
        '''Iterates over the tree and changes depth value for each. This will set the depth in the tree object.'''
        self.depth = 0

        Tree.__rec_calc_depth(self)
        return
        
        
    def __rec_calc_depth(tree, depth=0):
        
        depth += 1
        tree.depth = depth

        if tree.left is not None:
            left_depth = Tree.__rec_calc_depth(tree.left, depth)
        
        if tree.right is not None:
            right_depth = Tree.__rec_calc_depth(tree.right, depth)

        print(f"The node with value '{tree.value}' has depth {tree.depth}")
        return 
    
    
    def balance_tree(tree):
        '''balances current node'''
        
        Tree.calc_balance(tree)

        if (tree.balance >= 2) and (tree.right.balance in [0,1]):
            Tree.__rot_left(tree)
            return

        if (tree.balance >= 2) and (tree.right.balance == -1):
            Tree.__rot_right(tree.right)
            Tree.__rot_left(tree)
            return

        if (tree.balance <= -2) and (tree.right.balance in [-1,0]):
            Tree.__rot_right(tree)
            return

        if (tree.balance <= -2) and (tree.right.balance == 1):
            Tree.__rot_left(tree.left)
            Tree.__rot_right(tree)
            return
    
    
    def calc_height(tree) -> int:
        '''Returns height of provided node.'''
        
        left_height = 0
        right_height = 0

        if tree is None:
            return 0

        if tree.left is not None:
            left_height = Tree.calc_height(tree.left) + 1
        
        if tree.right is not None:
            right_height = Tree.calc_height(tree.right) + 1

        #print(f"left: {left_height}, right: {right_height}")
        result = max(left_height, right_height)

        print(f"The node '{tree.value}' has height: '{result}'")

        return result


    def __rot_right(node):
        pass

    def __rot_left(node):
        pass

    def calc_balance(tree):
        '''Calculates balance of current node. Returns True if its still a valid AVL-Tree'''
        tree.balance = Tree.calc_height(tree.right) - Tree.calc_height(tree.left)
        print(f"Node '{tree.value}' has balance: '{tree.balance}'")
        

    def export(self) -> tuple():
        '''Returns tuple containing the entire tree (value, left, right)'''

        left_tuple = None
        right_tuple = None

        if self.left is not None:
            left_tuple = self.left.export()

        if self.right is not None:
            right_tuple = self.right.export()

        return (self.value, left_tuple, right_tuple)

    
    def print(self):
        '''Attempts to print the tree.'''
        data = self.export()

        # oof i dont even know where to start