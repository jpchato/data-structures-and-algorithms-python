class IsEmptyError(Exception):
    pass

class Stack():

    class Node:
        def __init__(self, element, _next):
            self.element = element
            self._next = _next

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IsEmptyError('The stack is empty, cannot pop')
        result = self.head.element
        self.head = self.head._next
        self.size -= 1
        return result

    def peek(self):
        if self.is_empty():
            raise IsEmptyError("Stack is empty, cannot retrieve element")
        return self.head.element

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new = self.Node(element, None)
        if self.is_empty():
            self.head = new
        else:
            self.tail._next = new
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IsEmptyError("Queue empty, cannot dequeue")
        result = self.head.element
        self.head = self.head._next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return result

    def peek(self):
        if self.is_empty():
            raise IsEmptyError("Queue empty, nothing to peek at")
        return self.head.element
