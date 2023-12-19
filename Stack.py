from LinkedList import *


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        self.stack.insertat(0, Node(value=value))

    def pop(self):
        node = self.stack.deleteat(0)
        if node == None:
            return
        return node.get_value()
    

class Queue:
    def __init__(self):
        self.queue = LinkedList()
        self.size = 0
    
    def enqueue(self, value):
        self.queue.insertlast(Node(value=value))
        self.size += 1

    def dequeue(self):
        node = self.queue.deleteat(0)
        if node == None:
            return
        self.size -= 1
        return node.get_value()
    
    def get_size(self):
        return self.size


if __name__ == '__main__':
    q = Queue()
    q.enqueue(2)
    q.enqueue(5)
    q.enqueue(2)
    q.enqueue(7)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())