class Node:
    def __init__(self, value=None, next_node=None, prev_node=None, ishead=False, istail=False):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
        self.ishead = ishead
        self.istail = istail

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_prev(self):
        return self.prev_node
    
    def set_prev(self, prev_node):
        self.prev_node = prev_node


class LinkedList:
    def __init__(self):
        self.tail = Node(None, None, istail=True)
        self.head = Node(None, self.tail, ishead=True)

    def searchat(self, idx):
        node = self.head
        for i in range(idx):
            if node.istail:
                print('IndexError: Index out of bounds')
                return
            node = node.get_next()
        return node

    def insertat(self, idx, new_node):
        node = self.head
        for i in range(idx):
            node = node.get_next()
            if node.istail:
                print('IndexError: Index out of bounds')
                return
        next_node = node.get_next()
        node.set_next(new_node)
        new_node.set_next(next_node)

    def deleteat(self, idx):
        node = self.head
        for i in range(idx):
            node = node.get_next()
            if node.get_next().istail:
                print('IndexError: Index out of bounds')
                return
        delnode = node.get_next()
        if delnode.istail:
            return
        node.set_next(delnode.get_next())
        return delnode

    def insertlast(self, new_node):
        node = self.head
        while not node.get_next().istail:
            node = node.get_next()
        node.set_next(new_node)
        new_node.set_next(self.tail)

    def print_nodes(self):
        node = self.head.get_next()
        while node != self.tail:
            print(node.get_value())
            node = node.get_next()


class DoublyLinkedList: # to be implemented
    def __init__(self):
        self.tail = Node(None, None, self.head, istail=True)
        self.head = Node(None, self.tail, ishead=True)

    def searchat(self, idx):
        node = self.head
        for i in range(idx):
            if node.istail:
                print('IndexError: Index out of bounds')
                return
            node = node.get_next()
        return node

    def insertat(self, idx, new_node):
        node = self.head
        for i in range(idx):
            node = node.get_next()
            if node.istail:
                print('IndexError: Index out of bounds')
                return
        next_node = node.get_next()
        node.set_next(new_node)
        new_node.set_next(next_node)

    def deleteat(self, idx):
        node = self.head
        for i in range(idx):
            node = node.get_next()
            if node.get_next().istail:
                print('IndexError: Index out of bounds')
                return
        delnode = node.get_next()
        node.set_next(delnode.get_next())
        return delnode

    def insertlast(self, new_node):
        node = self.head
        while not node.get_next().istail:
            node = node.get_next()
        node.set_next(new_node)
        new_node.set_next(self.tail)

    def deletelast(self):
        pass # to be implemented

    def print_nodes(self):
        node = self.head.get_next()
        while node != self.tail:
            print(node.get_value())
            node = node.get_next()


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insertat(0, Node(value=2))
    linked_list.insertat(0, Node(value=5))
    linked_list.insertat(0, Node(value=3))
    linked_list.insertat(0, Node(value=4))
    linked_list.insertat(0, Node(value=21))
    linked_list.insertlast(Node(value=24323))
    linked_list.print_nodes()










