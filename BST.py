from BinaryTree import BTNode

class BinarySearchTree:
    def __init__(self):
        self.BST = BTNode()

    def insert(self, value, current_node=None):
        if current_node == None:
            current_node = self.BST

        if current_node.get_value() == None:
            current_node.set_value(value)
            return
        
        if current_node.get_value() > value:
            if current_node.get_left() == None:
                current_node.set_left(BTNode(value,current_node))
                return
            self.insert(value, current_node.get_left())
            return
        
        elif current_node.get_value() < value:
            if current_node.get_right() == None:
                current_node.set_right(BTNode(value,current_node))
                return
            self.insert(value, current_node.get_right())
            return
        
        else:
            print('Already exists.')
            return
        
    def search(self, value, current_node=None):
        if current_node == None:
            current_node = self.BST

        if current_node.get_value() == value:
            return True
        
        elif current_node.get_value() > value:
            if current_node.get_left() == None:
                print('There is no', value)
                return False
            return self.search(value, current_node.get_left())
        
        elif current_node.get_value() < value:
            if current_node.get_right() == None:
                print('There is no', value)
                return False
            return self.search(value, current_node.get_right())
        
    def delete(self, value, current_node=None):
        if current_node == None:
            current_node = self.BST
        
        if current_node.get_value() == value:
            # Case 1. no child node.
            if current_node.get_left() == None and current_node.get_right() == None:
                if current_node.get_parent().get_left() == current_node:
                    current_node.get_parent().set_left(None)
                elif current_node.get_parent().get_right() == current_node:
                    current_node.get_parent().set_right(None)
                else: # Root node case
                    self.BST = BTNode()
                return
            
            # Case 2. has one child node.
            elif current_node.get_left() == None:
                if current_node.get_parent() == None: # Root node case
                    self.BST = current_node.get_right()
                elif current_node.get_parent().get_left() == current_node:
                    current_node.get_parent().set_left(current_node.get_right())
                elif current_node.get_parent().get_right() == current_node:
                    current_node.get_parent().set_right(current_node.get_right())
                return
            elif current_node.get_right() == None:
                if current_node.get_parent() == None: # Root node case
                    self.BST = current_node.get_left()
                elif current_node.get_parent().get_left() == current_node:
                    current_node.get_parent().set_left(current_node.get_left())
                elif current_node.get_parent().get_right() == current_node:
                    current_node.get_parent().set_right(current_node.get_left())
                else: # Root node case
                    self.BST = current_node.get_left()
                return


            # Case 3. has multiple children nodes.
            else:
                # Either find min in right half tree or find max in left half tree.
                if current_node.get_right() != None:
                    min = self.find_min(current_node.get_right())
                    current_node.set_value(min.get_value())
                    self.delete(min.get_value(),min)

                elif current_node.get_left() != None:
                    max = self.find_max(current_node.get_left())
                    current_node.set_value(max.get_value())
                    self.delete(max.get_value(),max)

                
        elif current_node.get_value() > value:
            self.delete(value, current_node.get_left())
            return
        
        elif current_node.get_value() < value:
            self.delete(value, current_node.get_right())
            return
                

            
    def traverse(self, mode='inorder', node=None, sep=''):
        if node==None:
            node = self.BST

        if mode=='inorder':
            if node.get_left() != None:
                self.traverse(mode=mode, node=node.get_left(), sep=sep)
            print(node.get_value(), end=sep)
            if node.get_right() != None:
                self.traverse(mode=mode, node=node.get_right(), sep=sep)
            return

        elif mode=='preorder':
            print(node.get_value(), end=sep)
            if node.get_left() != None:
                self.traverse(mode=mode, node=node.get_left(), sep=sep)
            if node.get_right() != None:
                self.traverse(mode=mode, node=node.get_right(), sep=sep)
            return

        elif mode=='postorder':
            if node.get_left() != None:
                self.traverse(mode=mode, node=node.get_left(), sep=sep)
            if node.get_right() != None:
                self.traverse(mode=mode, node=node.get_right(), sep=sep)
            print(node.get_value(), end=sep)
            return

        else:
            print('Specify a mode.')
            return

    def find_min(self, node=None):
        if node==None:
            node=self.BST

        while node.get_left() != None:
            node = node.get_left()
        
        return node
    
    def find_max(self, node=None):
        if node==None:
            node=self.BST

        while node.get_right() != None:
            node = node.get_right()

        return node


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.insert(25)
    bst.insert(1)
    bst.insert(7)
    bst.insert(5)
    bst.insert(8)

    print('====First=====')
    bst.traverse(sep=', ')
    print()
    print('====Delete 3=====')
    bst.delete(3)
    bst.traverse(sep=', ')
    print()
    print('===============')
    print(bst.search(1))
    bst.traverse('postorder', sep=', ')
    print()
    bst.delete(1)
    bst.delete(2)
    bst.delete(5)
    bst.delete(8)
    bst.delete(25)
    print('===Delete 1 2 5 8 25====')
    bst.traverse(sep=', ')
    print()
    bst.delete(4)
    print('===Delete 4(Root node)====')
    bst.traverse(sep=', ')
    print()
    bst.delete(7)
    bst.delete(25)
    print('=====Delete All====')
    bst.traverse()
    print()