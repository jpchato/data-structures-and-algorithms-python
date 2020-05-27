class PseudoQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop() 

r = PseudoQueue()
r.enqueue(90)
r.enqueue(78)
r.enqueue(79)
print(r.dequeue())
r.enqueue(69)
print(r.dequeue())