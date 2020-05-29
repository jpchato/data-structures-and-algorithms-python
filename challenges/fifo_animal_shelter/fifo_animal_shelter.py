class Node:
    def __init__(self, value, next_=None):
        self.value = value 
        self.next = next_

class IsEmptyError(Exception):
    pass

# Used from class 11 code review
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.is_empty():
            raise IsEmptyError("Cannot pop from empty stack")
        outgoing = self.top
        self.top = self.top.next_
        return outgoing.value

    def peek(self):
        if self.is_empty():
            raise IsEmptyError("Cannot peek an empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None
    
    
# Used from class 11 code review
class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
    
    def enqueue(self, value):
        node = Node(value)
        if self._rear:
            self._rear.next = node
            self._rear = node
        else:
            self._rear = node
            self._front = node

    def dequeue(self):
        if not self._front: 
            raise IsEmptyError("Cannot dequeue from an empty queue")
        exiting = self._front
        self._front = self._front.next
        exiting.next = None
        return exiting.value

    def peek(self):
        if not self._front:
            raise IsEmptyError("Cannot peek at an empty queue")
        return self._front.value

    def is_empty(self):
        return self._front == None

class Dog:
    def __init__(self):
        self.name = "Dog"

class Cat:
    def __init__(self):
        self.name = "cat"

class AnimalShelter:
    def __init__(self):
        self._front = None
        self._rear = None

    def enqueue_pet(self, animal):
        if animal == "Dog" or animal == "Cat":
            self.enqueue(animal)
            return
        raise Exception("Cats and dogs only")

    def dequeue_pet(self, pref):
        if pref != "Dog" and pref != "Cat":
            return null


        
    