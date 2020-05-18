class LinkedList:

    def __init__(self):
        self.head = None

    #  Get in the habit of having a REPR for every class -JB
    def __repr__(self):
        return f"LinkedList : {self.head}"

    def __str__(self):
        res = ""
        current = self.head
        while current:
            # res += f"{{}}"
            res += "{ " + str(current.value) + " } -> "
            current = current.next
        return res + "NULL"

    #  self.head parameter is first
    def insert(self, value, next):
        self.head = Node(value, self.head)

    # solution found @ geeksforgeeks.org/search-an-element-in-a-linkedlist-iterative-and-recursive/
    def includes(self, value):
        current = self.head
        while current != None
            if current.value = value
                return True
            current = current.next
        return False


class Node:
    # value
    # next

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __repr__(self):
        return f"{self.value} : {self.next}"
