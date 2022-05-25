class Tree():

    def __init__(self, value=None):
        '''Creates new tree root'''
        
        self.value = value
        self.left = None
        self.right = None
        self.balance = 0
    

    def insert(self, value):
        '''Insert value into current tree'''

        # if list was provided, just iterate over it multiple times
        if isinstance(value, list):
            print("working with list!")
            for no in value:
                self.insert(no)
                self.export()
            return
        
        if self.value is None:
            self.value = value
            return
        
        if value == self.value:
            print("Value already found. REEEEEEEEEEEEEEEEEEEEEE")
            return

        # left
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
                return
            self.left.insert(value)
            return
            
        # right
        if value > self.value:
            if self.right is None:
                self.right = Tree(value)
                return
            self.right.insert(value)

    
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
    

    def delete(self, value) -> bool:
        
        if self.value == value:
            # this should only happen if this is the root of the tree
            result = self.__delete_root()

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
            tree.right = Tree.find_successor(next_node)
            return True
        
        return Tree.__delete_node(next_node, value)
        

    def __delete_root(self):
        if self.right is None and self.left is None:
                self.value == None
                return
            
        # right is None
        if self.right is None:
            self.value = self.left.value
            self.right = self.left.right
            self.left = self.left.left
            return
        
        # left is None
        if self.left is None:
            self.value = self.right.value
            self.left = self.right.left
            self.right = self.right.right
            return

        # right.left None
        if self.right.left is None:
            self.value = self.right.value
            self.right = self.right.right

        successor = Tree.find_successor(self)

        self.value = successor.value
        self.right = successor.right


    def find_successor(tree):
        '''Searches for successor and replaces deleted object'''
        
        # give parent current branches
        if tree.right.left is None:
            return tree.right

        return Tree.__rec_find_successor(tree.right)


    def __rec_find_successor(tree):
        
        if tree.left.left is None:
            
            result = tree.left

            # assign right of successor to left of its parent
            tree.left = tree.left.right
            
            return result
        
        return tree.__rec_find_successor(tree.left)


    def export(self) -> tuple():
        '''Returns tuple containing the entire tree (value, left, right)'''

        left_tuple = None
        right_tuple = None

        if self.left is not None:
            left_tuple = self.left.export()

        if self.right is not None:
            right_tuple = self.right.export()

        return (self.value, left_tuple, right_tuple)