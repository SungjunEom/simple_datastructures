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
        
    def delete(self, value, current_node=None): # To be replaced
        if current_node == None:
            current_node = self.BST
        current_value = current_node.get_value()
        if current_value == value:
            parent = current_node.get_parent()
            if parent.get_left() == current_node:
                target = current_node
                while target.get_right() != None:
                    target = target.get_right()
                if target.get_left() == None:
                    current_node.set_value(target.get_value())
                    target.get_parent().set_right(None)
                    return
                else:
                    current_node.set_value(target.get_value())
                    target.get_parent().set_right(target.get_left())
                    return
            elif parent.get_right() == current_node:
                target = current_node
                while target.get_left() != None:
                    target = target.get_left()
                if target.get_right() == None:
                    current_node.set_value(target.get_value())
                    target.get_parent().set_left(None)
                    return
                else:
                    current_node.set_value(target.get_value())
                    target.get_parent().set_left(target.get_right())
                    return
        elif current_value > value:
            if current_node.get_left() == None:
                return False
            current_node = current_node.get_left()
            return self.delete(value, current_node)
        elif current_value < value:
            if current_node.get_right() == None:
                return False
            current_node = current_node.get_right()
            return self.delete(value, current_node)
            
    def traverse(self, mode='inorder', node=None):
        if node==None:
            node = self.BST

        if mode=='inorder':
            if node.get_left() != None:
                self.traverse(mode=mode, node=node.get_left())
            print(node.get_value())
            if node.get_right() != None:
                self.traverse(mode=mode, node=node.get_right())

        elif mode=='preorder':
            print(node.get_value())
            if node.get_left() != None:
                self.traverse(mode=mode, node=node.get_left())
            if node.get_right() != None:
                self.traverse(mode=mode, node=node.get_right())

        elif mode=='postorder':
            if node.get_left() != None:
                self.traverse(mode=mode, node=node.get_left())
            if node.get_right() != None:
                self.traverse(mode=mode, node=node.get_right())
            print(node.get_value())

        else:
            print('Specify a mode.')

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
    bst.delete(3)
    print(bst.search(1))
    bst.traverse('postorder')