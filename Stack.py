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
    
    def enqueue(self, value):
        self.queue.insertlast(Node(value=value))

    def dequeue(self):
        node = self.queue.deleteat(0)
        if node == None:
            return
        return node.get_value()


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