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
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    # solution found @ https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
    def append_to_list(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    # solution found @ https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
    def insert_after(self, previous_node, new_value):
        if previous_node is None:
            return
        new_node = Node(new_value)
        new_node.next = previous_node.next
        previous_node.next = new_node

    


class Node:
    # value
    # next

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __repr__(self):
        return f"{self.value} : {self.next}"
